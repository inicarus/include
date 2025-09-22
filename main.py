# main.py - نسخه نهایی و تمیز شده برای تلگرام

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

# --- تنظیمات ---
USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36']
COUNTRY_FLAGS = {
    "US": "🇺🇸", "DE": "🇩🇪", "FR": "🇫🇷", "NL": "🇳🇱", "GB": "🇬🇧",
    "RU": "🇷🇺", "CA": "🇨🇦", "FI": "🇫🇮", "IR": "🇮🇷", "SE": "🇸🇪",
}

# --- توابع کمکی ---
def clean_line(line):
    if not line: return ""
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

def get_country_from_ip(ip):
    try:
        if not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
             ip = socket.gethostbyname(ip)
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return COUNTRY_FLAGS.get(data.get('countryCode'), '🌍')
        return '🌍'
    except Exception:
        return '🌍'

def process_proxy_line(line):
    """یک خط پروکسی را پردازش، تست و اطلاعات آن را برمی‌گرداند."""
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

# --- توابع اصلی ---
def fetch_proxies_from_sources(text_urls, telegram_urls):
    raw_lines = set()

    # 1. دریافت از منابع متنی
    for url in text_urls:
        try:
            logging.info(f"Fetching from text source: {url}")
            response = requests.get(url, timeout=10)
            if response.ok:
                raw_lines.update(response.text.splitlines())
        except Exception as e:
            logging.warning(f"Failed to fetch {url}: {e}")

    # 2. دریافت از کانال‌های تلگرام
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'user-agent={random.choice(USER_AGENTS)}')
    
    try:
        with webdriver.Chrome(options=options) as driver:
            for url in telegram_urls:
                try:
                    logging.info(f"Fetching from Telegram channel: {url}")
                    driver.get(url)
                    time.sleep(5) # زمان برای لود شدن محتوای داینامیک
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    proxy_elements = soup.find_all('a', href=re.compile(r'tg://proxy'))
                    raw_lines.update([element.get('href') for element in proxy_elements])
                except Exception as e:
                    logging.warning(f"Failed to fetch {url}: {e}")
    except WebDriverException as e:
        logging.error(f"WebDriver could not be initialized: {e}")


    # 3. پردازش و تست موازی پروکسی‌ها
    processed_proxies = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_line = {executor.submit(process_proxy_line, line): line for line in raw_lines if line}
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
        button = {'text': f"{proxy['country']} اتصال {i}", 'url': url}
        row.append(button)
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    
    reply_markup = {'inline_keyboard': keyboard}
    
    url_api = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': channel_id, 'text': header, 'reply_markup': json.dumps(reply_markup)}
    
    try:
        response = requests.post(url_api, json=payload, timeout=20)
        if response.json().get('ok'):
            logging.info("Successfully sent proxies to Telegram channel.")
        else:
            logging.error(f"Telegram API error: {response.text}")
    except requests.RequestException as e:
        logging.error(f"Failed to send message to Telegram: {e}")

# --- اجرای اسکریپت ---
if __name__ == "__main__":
    text_sources = [
        "https://raw.githubusercontent.com/MhdiTaheri/ProxyCollector/main/proxy.txt",
        "https://raw.githubusercontent.com/SoliSpirit/mtproto/master/all_proxies.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/mtproto.json",
    ]
    telegram_sources = [
        "https://t.me/s/ProxyMTProto",
        "https://t.me/s/iRoProxy",
        "https://t.me/s/proxyskyy",
        "https://t.me/s/HiProxy",
    ]
    
    active_proxies = fetch_proxies_from_sources(text_sources, telegram_sources)
    
    if active_proxies:
        logging.info(f"Total unique active proxies found: {len(active_proxies)}")
        active_proxies.sort(key=lambda p: p['country'])
        save_proxies_to_file(active_proxies)
        send_proxies_to_channel(active_proxies)
    else:
        logging.warning("No active proxies found. Nothing to save or send.")
