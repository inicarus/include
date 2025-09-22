# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 10:00 31-06-1404)

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
| 1 | `prmusic.ir` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=prmusic.ir&port=80&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 2 | `ns1.saladin-net.ir.` | `6773` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=ns1.saladin-net.ir.&port=6773&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 3 | `171.22.183.79` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=171.22.183.79&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 4 | `3733377078.ir.ir.ir.ir.ir.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=3733377078.ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | `komatso-japan.www.google.com.ganool-com.info` | `300` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=komatso-japan.www.google.com.ganool-com.info&port=300&secret=eeRigzNJvXrFGRMCIMJdEARueWVrdGFuZXQuY29tZmFyYTrhdi5jb212YZ6ubmFqXeEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 6 | `91.98.18.94` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.18.94&port=8888&secret=ee5lrPbFdb1vizwd3HEHowtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `yavar.pas-netiran.co.uk` | `23` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yavar.pas-netiran.co.uk&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 8 | `private.engpoli.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=private.engpoli.ir&port=443&secret=eeDDNEgYdJvXrFGRMCIMJQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 9 | `9.mm.brobalair.store` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=9.mm.brobalair.store&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `163.5.31.33` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=163.5.31.33&port=8443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `91.99.205.245` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.205.245&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 12 | `188.92.28.192` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=188.92.28.192&port=8443&secret=ee89c113a951ffbbe37a9aeb56b178435662696e672e636f6d) |
| 13 | `95.134.130.87` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=95.134.130.87&port=443&secret=3968da1760170c9b7b118860006e2e63) |
| 14 | `91.98.74.115` | `98` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.74.115&port=98&secret=7qqhvqqqqqqKqqqrqqyqqoh3d3cuY2xvdWRmbGFyZS5jb20sZGl2YXJjZG4uY29tLHd3dy5zcGVlZHRlc3QubmV0LHNuYXBwLmly) |
| 15 | `locano-koper-zhopbis-manotor.solder-chopan.rang-mavar-zhos.info` | `300` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=locano-koper-zhopbis-manotor.solder-chopan.rang-mavar-zhos.info&port=300&secret=eeRigzNJvXrFGRMCIMJdEA) |
| 16 | `140.233.167.152` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=140.233.167.152&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 17 | `128.140.44.219` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=128.140.44.219&port=443&secret=ee52c867dc75983faf4bb37f91d5164f0970726f746f6e6d61696c726d657a336c6f74636369707368746b6c65656765746f6c62373366756972676a3772346f34766675376f7a79642e6f6e696f6e) |
| 18 | `178.130.43.112` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=178.130.43.112&port=443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 19 | `14.102.10.132` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.132&port=85&secret=ee00ff000fffff00fff5555ffffffffff5662e6b6f2d2d) |
| 20 | `pofak.opensusebase.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pofak.opensusebase.co.uk&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
