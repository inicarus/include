# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 14:39 30-06-1404)

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/python-3.9-blue" alt="Python 3.9" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions Welcome" />
  <img src="https://img.shields.io/badge/Proxy%20Scraper-Running-green" alt="Proxy Scraper" />
  <img src="https://github.com/inicarus/khoda/actions/workflows/main.yml/badge.svg" alt="Proxy Scraper Workflow" />
  <img src="https://img.shields.io/github/last-commit/inicarus/khoda" alt="GitHub Last Commit" />
  <img src="https://img.shields.io/github/issues/inicarus/khoda" alt="GitHub Issues" />
</p>

این پروژه یک اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع مختلف است. پروکسی‌ها در فایل `proxy.txt` ذخیره می‌شوند و هر ۳ ساعت به‌صورت خودکار به‌روزرسانی می‌شوند.

## ✨ درباره پروژه

این اسکریپت با استفاده از `requests` برای منابع متنی و `selenium` برای کانال‌های تلگرام، پروکسی‌های MTProto را جمع‌آوری می‌کند. فقط پروکسی‌های فعال و آنلاین ذخیره شده و نتایج در فایل `proxy.txt` قرار می‌گیرند. این فرآیند به‌صورت خودکار با **GitHub Actions** هر ۳ ساعت اجرا می‌شود.

## 🚀 ویژگی‌ها
- 🌐 جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- ✅ **بررسی وضعیت آنلاین بودن پروکسی‌ها** قبل از ذخیره
- 🔄 به‌روزرسانی خودکار هر ۳ ساعت
- 🗑 حذف پروکسی‌های تکراری
- 📱 رابط کاربری مدرن و تعاملی برای مشاهده و استفاده از پروکسی‌ها

## 🛠 نحوه استفاده
1. برای مشاهده لیست پروکسی‌ها به صورت آنلاین، به این صفحه مراجعه کنید: **[صفحه پروکسی‌ها](https://inicarus.github.io/khoda/)**
2. فایل `proxy.txt` را از **[اینجا](proxy.txt)** دانلود کنید.
3. لینک‌های پروکسی را در کلاینت تلگرام خود وارد کنید.
4. در جدول زیر، روی **لینک پروکسی** کلیک کنید تا به تلگرام هدایت شوید.

## 📈 نمونه پروکسی‌ها
جدول زیر نمونه‌ای از ۲۰ پروکسی فعال از فایل `proxy.txt` را نمایش می‌دهد. این جدول به صورت خودکار به‌روز می‌شود.

| # | سرور (Server) | پورت (Port) | وضعیت | لینک پروکسی |
|---|---|---|---|---|
| 1 | `85.198.108.252` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=85.198.108.252&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 2 | `proxy.codex-vpn.ru` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=proxy.codex-vpn.ru&port=443&secret=ee3fbe95e68e560b9b58e408e13b22ad0d70726f78792d736e692e636f6465782d76706e2e7275) |
| 3 | `bede6.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bede6.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 4 | `snowa.samsungp.ir` | `4030` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=snowa.samsungp.ir&port=4030&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 5 | `7777.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7777.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | `146.103.106.90` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.106.90&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `65.108.84.7` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.108.84.7&port=443&secret=ee0000000000000000000000000000000064656570696e73616e652e636f6d) |
| 8 | `14.102.10.45` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.45&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `dedicated.engpoli.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=dedicated.engpoli.ir&port=443&secret=eeDDNEgYdJvXrFGRMCIMJQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 10 | `chat.nespresso-cups.co.uk` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=chat.nespresso-cups.co.uk&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `systemfull.gjesus.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=systemfull.gjesus.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 12 | `uplink-bandwidth.pucon.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=uplink-bandwidth.pucon.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 13 | `14.102.10.13` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.13&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 14 | `89.110.113.224` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.110.113.224&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 15 | `37333770768.ir.ir.ir.ir.ir.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=37333770768.ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 16 | `cloudflare.termiusclient.co.uk` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloudflare.termiusclient.co.uk&port=9741&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 17 | `14.102.10.145` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.145&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 18 | `14.102.10.104` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.104&port=85&secret=7ggggggggggggggggggggghpdmlmLmly) |
| 19 | `cloud-hosting.sibiu.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=cloud-hosting.sibiu.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 20 | `7887798711.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7887798711.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
