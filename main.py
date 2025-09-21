 # main.py

import requests
from bs4 import BeautifulSoup
import re
import random
import time
import logging
from datetime import datetime
import pytz
import jdatetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import unicodedata
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def clean_line(line):
    line = line.strip().replace('\r', '').replace('\n', '')
    line = ''.join(c for c in line if unicodedata.category(c)[0] != 'C')
    return line

def check_proxy_status(server, port, timeout=3):  
    """Check if a proxy server is online by attempting a connection."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((server, int(port)))
        sock.close()
        if result == 0:
            logging.info(f"Proxy {server}:{port} is online")
            return True
        else:
            logging.warning(f"Proxy {server}:{port} is offline or unreachable")
            return False
    except (socket.timeout, socket.gaierror, ConnectionRefusedError, OSError) as e:
        logging.error(f"Error checking proxy {server}:{port}: {e}")
        return False

def fetch_proxies_from_text_urls(urls):
    all_links = []
    headers = {'User-Agent': get_random_user_agent()}
    pattern = r'^(tg://proxy|https://t\.me/proxy)\?server=[^&]+&port=\d+(&secret=.+)$'
    
    for url in urls:
        try:
            logging.info(f"Fetching proxies from {url}")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            if url.endswith('.json'):
                try:
                    data = response.json()
                    proxy_checks = []
                    for item in data:
                        server = item.get('host')
                        port = item.get('port')
                        secret = item.get('secret')
                        if server and port and secret:
                            proxy_link = f"tg://proxy?server={server}&port={port}&secret={secret}"
                            proxy_checks.append((proxy_link, server, port))
                        else:
                            logging.debug(f"Skipping invalid JSON proxy entry: {item}")
                    
                    with ThreadPoolExecutor(max_workers=30) as executor:
                        future_to_proxy = {executor.submit(check_proxy_status, server, port): (proxy, server, port) for proxy, server, port in proxy_checks}
                        for future in as_completed(future_to_proxy):
                            proxy, server, port_num = future_to_proxy[future]
                            try:
                                if future.result():
                                    all_links.append(proxy)
                                    logging.info(f"Valid and online proxy from JSON: {proxy}")
                            except Exception as e:
                                logging.error(f"Error checking proxy {proxy}: {e}")
                
                except json.JSONDecodeError as e:
                    logging.error(f"Invalid JSON format in {url}: {e}")
            else:
                lines = response.text.splitlines()
                proxy_checks = []
                
                for line in lines:
                    line = clean_line(line)
                    if not line:
                        continue
                    if re.match(pattern, line):
                        match = re.match(r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=.+$', line)
                        if match:
                            server, port = match.groups()
                            proxy_checks.append((line, server, port))
                        else:
                            logging.debug(f"Invalid or skipped proxy: {line} (does not match pattern)")
                    else:
                        logging.debug(f"Invalid or skipped proxy: {line} (does not match pattern)")
                
                with ThreadPoolExecutor(max_workers=30) as executor:
                    future_to_proxy = {executor.submit(check_proxy_status, server, port): (line, server, port) for line, server, port in proxy_checks}
                    for future in as_completed(future_to_proxy):
                        line, server, port_num = future_to_proxy[future]
                        try:
                            if future.result():
                                all_links.append(line)
                                logging.info(f"Valid and online proxy found: {line}")
                        except Exception as e:
                            logging.error(f"Error checking proxy {line}: {e}")
            
            logging.info(f"Fetched {len(all_links)} valid and online MTProto proxies from {url}")
        except requests.RequestException as e:
            logging.error(f"HTTP error fetching {url}: {e}")
        time.sleep(random.uniform(0.5, 1.0))
    return all_links

def fetch_proxies_from_telegram_channel(url):
    proxies = []
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={get_random_user_agent()}')
    
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        logging.info(f"Opened {url}")
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(5):  
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  
            new_height = driver.execute_script("return document.body.scrollHeight")
            logging.info(f"Scrolled {url}, attempt {i+1}, new height: {new_height}")
            if new_height == last_height:
                logging.info(f"No more content to load for {url}")
                break
            last_height = new_height
        
        page_source = driver.page_source
        if "CAPTCHA" in page_source or "recaptcha" in page_source.lower():
            logging.warning(f"CAPTCHA detected on {url}")
        
        soup = BeautifulSoup(page_source, 'html.parser')
        pattern = r'^(tg://proxy|https://t\.me/proxy)\?server=[^&]+&port=\d+(&secret=.+)$'
        proxy_elements = soup.find_all('a', href=re.compile(pattern))
        
        proxy_checks = []
        for element in proxy_elements:
            proxy = element.get('href')
            match = re.match(r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=.+$', proxy)
            if match:
                server, port = match.groups()
                proxy_checks.append((proxy, server, port))
        
        with ThreadPoolExecutor(max_workers=30) as executor:  
            future_to_proxy = {executor.submit(check_proxy_status, server, port): (proxy, server, port) for proxy, server, port in proxy_checks}
            for future in as_completed(future_to_proxy):
                proxy, server, port_num = future_to_proxy[future]
                try:
                    if future.result():
                        proxies.append(proxy)
                        logging.info(f"Valid and online proxy found from Telegram: {proxy}")
                except Exception as e:
                    logging.error(f"Error checking proxy {proxy}: {e}")
        
        logging.info(f"Fetched {len(proxies)} valid and online MTProto proxies from {url}")
    except WebDriverException as e:
        logging.error(f"WebDriver error fetching {url}: {e}")
    except Exception as e:
        logging.error(f"General error fetching {url}: {e}")
    finally:
        if driver:
            driver.quit()
    time.sleep(random.uniform(0.5, 1.0))  
    return proxies

def save_proxies_to_file(proxy_list, filename='proxy.txt'):
    try:
        unique_proxies = sorted(list(set(proxy_list)))
        with open(filename, 'w', encoding='utf-8') as file:
            for proxy in unique_proxies:
                file.write(proxy + '\n')
        logging.info(f"Saved {len(unique_proxies)} unique proxies to {filename}")
        return unique_proxies
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")
        return []

def update_readme(proxy_list):
    try:
        utc_now = datetime.now(pytz.UTC)
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_now = utc_now.astimezone(iran_tz)
        
        jalali_date = jdatetime.datetime.fromgregorian(datetime=iran_now)
        update_time_iran = jalali_date.strftime('%H:%M %d-%m-%Y')
        logging.info(f"Updating README with Iranian timestamp: {update_time_iran}")

        sample_proxies = random.sample(proxy_list, min(20, len(proxy_list))) if proxy_list else []
        table_rows = ""
        for i, proxy in enumerate(sample_proxies, 1):
            proxy_url = proxy.strip().replace('tg://proxy', 'https://t.me/proxy')
            match = re.match(r'^https://t\.me/proxy\?server=([^&]+)&port=(\d+).*$', proxy_url)
            if match:
                server, port = match.groups()
                table_rows += f"| {i} | `{server}` | `{port}` | ✅ فعال | [لینک پروکسی]({proxy_url}) |\n"
        
        readme_path = 'README.md'
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()

        # Safely replace the dynamic parts
        start_marker_time = "(آخرین بروزرسانی: "
        end_marker_time = ")"
        start_marker_table = "| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |\n|---|---|---|---|---|\n"
        end_marker_table = "\n> **💡 نکته**:"

        # Update time
        time_start_pos = readme_content.find(start_marker_time)
        if time_start_pos != -1:
            time_end_pos = readme_content.find(end_marker_time, time_start_pos)
            if time_end_pos != -1:
                readme_content = readme_content[:time_start_pos + len(start_marker_time)] + update_time_iran + readme_content[time_end_pos:]

        # Update table
        table_start_pos = readme_content.find(start_marker_table)
        if table_start_pos != -1:
            table_end_pos = readme_content.find(end_marker_table, table_start_pos)
            if table_end_pos != -1:
                new_table = start_marker_table + table_rows
                readme_content = readme_content[:table_start_pos] + new_table + readme_content[table_end_pos:]

        with open(readme_path, 'w', encoding='utf-8') as file:
            file.write(readme_content)
        logging.info("Successfully updated README.md")
    except Exception as e:
        logging.error(f"Error updating README.md: {e}")

if __name__ == "__main__":
    text_urls = [
        "https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt",
        "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json"
    ]
    
    telegram_urls = [
        "https://t.me/s/iporoto", "https://t.me/s/HiProxy", "https://t.me/s/iproxy",
        "https://t.me/s/iRoProxy", "https://t.me/s/proxyforopeta", "https://t.me/s/IRN_Proxy",
        "https://t.me/s/MProxy_ir", "https://t.me/s/ProxyHagh", "https://t.me/s/PyroProxy",
        "https://t.me/s/ProxyMTProto", "https://t.me/s/MTPro_XYZ", "https://t.me/s/vpns",
        "https://t.me/s/mtmvpn", "https://t.me/s/asr_proxy", "https://t.me/s/proxyskyy"
    ]
    
    text_proxies = fetch_proxies_from_text_urls(text_urls)
    
    telegram_proxies = []
    # Running Selenium in parallel can be resource-intensive, so we do it sequentially.
    for url in telegram_urls:
        proxies = fetch_proxies_from_telegram_channel(url)
        telegram_proxies.extend(proxies)
    
    all_proxies = list(set(text_proxies + telegram_proxies))
    
    active_proxies = save_proxies_to_file(all_proxies, filename='proxy.txt')
    
    # Check if we have active proxies before updating README
    if active_proxies:
        update_readme(active_proxies)
    else:
        logging.warning("No active proxies found, README will not be updated.")
