# main.py - نسخه ساده‌شده فقط برای تلگرام

import os
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

USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36']
COUNTRY_FLAGS = {
    "US": "🇺🇸", "DE": "🇩🇪", "FR": "🇫🇷", "NL": "🇳🇱", "GB": "🇬🇧",
    "RU": "🇷🇺", "CA": "🇨🇦", "FI": "🇫🇮", "IR": "🇮🇷", "SE": "🇸🇪",
}

def get_country_from_ip(ip):
    try:
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
             ip = socket.gethostbyname(ip)
        
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode", timeout=5)
        if response.status_code == 200:
            data = response.json()
            country_code = data.get('countryCode', 'XX')
            return COUNTRY_FLAGS.get(country_code, '🌍')
        return '🌍'
    except Exception:
        return '🌍'

def process_proxy_line(line):
    line = clean_line(line)
    pattern = r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=([a-zA-Z0-9\-_=]+)'
    match = re.match(pattern, line)
    if not match:
        return None
    
    server, port, secret = match.groups()
    
    if not check_proxy_status(server, port):
        return None
        
    country_flag = get_country_from_ip(server)
    
    return {
        "link": f"tg://proxy?server={server}&port={port}&secret={secret}",
        "country": country_flag
    }

def fetch_proxies_from_sources(text_urls, telegram_urls):
    raw_lines = []
    
    for url in text_urls:
        try:
            logging.info(f"Fetching from text source: {url}")
            response = requests.get(url, timeout=10)
            if response.ok:
                raw_lines.extend(response.text.splitlines())
        except Exception as e:
            logging.warning(f"Failed to fetch {url}: {e}")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={random.choice(USER_AGENTS)}')
    
    with webdriver.Chrome(options=options) as driver:
        for url in telegram_urls:
            try:
                logging.info(f"Fetching from Telegram channel: {url}")
                driver.get(url)
                time.sleep(5)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                proxy_elements = soup.find_all('a', href=re.compile(r'tg://proxy'))
                raw_lines.extend([element.get('href') for element in proxy_elements])
            except Exception as e:
                logging.warning(f"Failed to fetch {url}: {e}")

    processed_proxies = []
    unique_links = set(filter(None, raw_lines))
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_line = {executor.submit(process_proxy_line, line): line for line in unique_links}
        for future in as_completed(future_to_line):
            result = future.result()
            if result:
                processed_proxies.append(result)
                
    return processed_proxies

def save_proxies_to_file(proxies, filename='proxy.txt'):
    links = [p['link'] for p in proxies]
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(f"{link}\n" for link in sorted(links))
        logging.info(f"Saved {len(links)} proxies to {filename}")
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")

def send_proxies_to_channel(proxies):
    bot_token = os.getenv('BOT_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    
    if not bot_token or not channel_id:
        logging.warning("BOT_TOKEN or CHANNEL_ID not set. Skipping sending message.")
        return

    proxies_to_send = random.sample(proxies, min(16, len(proxies)))
    
    tehran_tz = pytz.timezone('Asia/Tehran')
    now_tehran = datetime.now(tehran_tz)
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now_tehran).strftime('%Y/%m/%d')
    current_time = now_tehran.strftime('%H:%M')
    
    header = f"""
╭⋟────𓄂ꪴꪰ𓆃────╮
 | 𓐄𓐅𓐆𓐇 PЯӨXYFĪG 𓐇𓐆𓐅𓐄 ⁮⁮⁮|
╰────────────⋞╯

     💀PʀᴏxʏSᴋᴜʟʟ💀 
❚⫘⫘⫘⫘⫘⫘⫘❚
        ☠️MTProto II☠️ 
           
▬▭▬▭𓐄🧌𓐄▭▬▭▬
{current_time} 𓍯 {jalali_date}
"""
    
    keyboard = []
    row = []
    for i, proxy in enumerate(proxies_to_send, 1):
        url = proxy['link'].replace('tg://proxy?', 'https://t.me/proxy?')
        button = {'text': f"{proxy['country']} اتصال {i + 1}", 'url': url}
        row.append(button)
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    
    reply_markup = {'inline_keyboard': keyboard}
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': channel_id, 'text': header, 'reply_markup': json.dumps(reply_markup)}
    
    try:
        response = requests.post(url, json=payload, timeout=20)
        if response.json().get('ok'):
            logging.info("Successfully sent proxies to Telegram channel.")
        else:
            logging.error(f"Telegram API error: {response.text}")
    except requests.RequestException as e:
        logging.error(f"Failed to send message to Telegram: {e}")

# --- توابع کمکی ---
def clean_line(line):
    line = line.strip().replace('\r', '').replace('\n', '')
    return ''.join(c for c in line if unicodedata.category(c)[0] != 'C')

def check_proxy_status(server, port, timeout=2):
    try:
        port_num = int(port)
        if not 0 < port_num <= 65535: return False
        with socket.create_connection((server, port_num), timeout=timeout):
            return True
    except (ValueError, socket.gaierror, socket.timeout, ConnectionRefusedError, OSError):
        return False

if __name__ == "__main__":
    text_sources = [
        "https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt",
        "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt",
    ]
    telegram_sources = [
        "https://t.me/s/ProxyMTProto",
        "https://t.me/s/iRoProxy",
    ]
    
    active_proxies = fetch_proxies_from_sources(text_sources, telegram_sources)
    
    if active_proxies:
        active_proxies.sort(key=lambda p: p['country'])
        save_proxies_to_file(active_proxies)
        send_proxies_to_channel(active_proxies)
    else:
        logging.warning("No active proxies found.")    proxies = []
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
        time.sleep(5)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        pattern = r'^(tg://proxy|https://t\.me/proxy)\?server=[^&]+&port=\d+(&secret=.+)$'
        proxy_elements = soup.find_all('a', href=re.compile(pattern))
        
        proxy_checks = []
        for element in proxy_elements:
            proxy = element.get('href')
            match = re.match(r'^(?:tg://proxy|https://t\.me/proxy)\?server=([^&]+)&port=(\d+)&secret=.+$', proxy)
            if match:
                proxy_checks.append((proxy, match.group(1), match.group(2)))
        
        with ThreadPoolExecutor(max_workers=30) as executor:
            future_to_proxy = {executor.submit(check_proxy_status, server, port): proxy for proxy, server, port in proxy_checks}
            for future in as_completed(future_to_proxy):
                if future.result():
                    proxies.append(future_to_proxy[future])
        
    except Exception as e:
        logging.error(f"Error fetching {url}: {e}")
    finally:
        if driver:
            driver.quit()
    return proxies

def save_proxies_to_file(proxy_list, filename='proxy.txt'):
    try:
        unique_proxies = sorted(list(set(proxy_list)))
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(f"{proxy}\n" for proxy in unique_proxies)
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

        start_marker_time = "(آخرین بروزرسانی: "
        end_marker_time = ")"
        start_marker_table = "| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |\n|---|---|---|---|---|\n"
        end_marker_table = "\n> **💡 نکته**:"

        time_start_pos = readme_content.find(start_marker_time)
        if time_start_pos != -1:
            time_end_pos = readme_content.find(end_marker_time, time_start_pos)
            if time_end_pos != -1:
                readme_content = readme_content[:time_start_pos + len(start_marker_time)] + update_time_iran + readme_content[time_end_pos:]

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

def create_message_header():
    tehran_tz = pytz.timezone('Asia/Tehran')
    now_tehran = datetime.now(tehran_tz)
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now_tehran).strftime('%Y/%m/%d')
    current_time = now_tehran.strftime('%H:%M:%S')
    header = f"""
╭⋟────𓄂ꪴꪰ𓆃────╮
 | 𓐄𓐅𓐆𓐇 PЯӨXYFĪG 𓐇𓐆𓐅𓐄 ⁮⁮⁮|
╰────────────⋞╯

     💀PʀᴏxʏSᴋᴜʟʟ💀 
❚⫘⫘⫘⫘⫘⫘⫘❚
        ☠️MTProto II☠️ 
           
▬▭▬▭𓐄🧌𓐄▭▬▭▬
{current_time} 𓍯 {jalali_date}
"""
    return header

def create_inline_keyboard(proxies):
    keyboard = []
    row = []
    for i, proxy_url in enumerate(proxies):
        url = proxy_url.replace('tg://proxy?', 'https://t.me/proxy?')
        button = {'text': f'🟢 اتصال {i + 1}', 'url': url}
        row.append(button)
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    return {'inline_keyboard': keyboard}

def send_proxies_to_channel(proxy_list):
    bot_token = os.getenv('BOT_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    
    if not bot_token or not channel_id:
        logging.warning("BOT_TOKEN or CHANNEL_ID not set. Skipping sending message to Telegram.")
        return

    if not proxy_list:
        logging.warning("Proxy list is empty. No proxies to send.")
        return

    logging.info(f"Preparing to send proxies to channel {channel_id}")
    
    proxies_to_send = random.sample(proxy_list, min(16, len(proxy_list)))
    
    message_text = create_message_header()
    reply_markup = create_inline_keyboard(proxies_to_send)
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': channel_id,
        'text': message_text,
        'reply_markup': json.dumps(reply_markup),
        'disable_web_page_preview': True
    }
    
    try:
        response = requests.post(url, json=payload, timeout=20)
        response.raise_for_status()
        if response.json().get('ok'):
            logging.info(f"Successfully sent {len(proxies_to_send)} proxies to the channel.")
        else:
            logging.error(f"Telegram API returned an error: {response.text}")
    except requests.RequestException as e:
        logging.error(f"Failed to send message to Telegram: {e}")

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
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(fetch_proxies_from_telegram_channel, url): url for url in telegram_urls}
        for future in as_completed(future_to_url):
            try:
                telegram_proxies.extend(future.result())
            except Exception as exc:
                logging.error(f'Fetching from {future_to_url[future]} generated an exception: {exc}')

    all_proxies = list(set(text_proxies + telegram_proxies))
    logging.info(f"Total unique active proxies found: {len(all_proxies)}")
    
    active_proxies = save_proxies_to_file(all_proxies, filename='proxy.txt')
    
    if active_proxies:
        update_readme(active_proxies)
        send_proxies_to_channel(active_proxies)
    else:
        logging.warning("No active proxies found. Nothing to update or send.")
