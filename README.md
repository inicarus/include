# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 16:04 30-06-1404)

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
| 1 | `213.206.138.54.paaawdreboot.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=213.206.138.54.paaawdreboot.ir&port=443&secret=eeXifpB2GBv9shh2kvi5lAtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `185.207.98.2.diskqavi.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.207.98.2.diskqavi.ir&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29t) |
| 3 | `91.238.92.238` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.238.92.238&port=155&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `1111.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=1111.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | `package.cbloudcdn.com` | `1000` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=package.cbloudcdn.com&port=1000&secret=7qi6jdKKygIxFalhsTItDWZ3d3cuY2Jsb3VkY2RuLmNvbQ) |
| 6 | `44.atousa4sam.co.uk` | `6773` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=44.atousa4sam.co.uk&port=6773&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `44.iropt-r.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=44.iropt-r.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmlkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ) |
| 8 | `157.90.0.57` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=157.90.0.57&port=155&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 9 | `45.153.33.39` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.153.33.39&port=155&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 10 | `77.238.230.158` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.238.230.158&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 11 | `7474.ir.koch.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7474.ir.koch.newdf12.info&port=8888&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 12 | `185.245.107.102` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.245.107.102&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 13 | `88.216.95.66.sorativip.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.216.95.66.sorativip.ir&port=443&secret=eeDDNEgYdJvXrFGRMCIMJQtY2RueWVrdGFuZXQuY29tZ) |
| 14 | `163.5.31.48` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=163.5.31.48&port=8443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `184.174.98.12` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=184.174.98.12&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 16 | `91.238.92.240` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.238.92.240&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 17 | `185.29.223.124` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.29.223.124&port=443&secret=7rJc31NLmTL5eReCJZJPndJ3d3cuZ29vZ2xlLmNvbQ) |
| 18 | `allinone.transiiantanialnmiomana.info` | `666` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=allinone.transiiantanialnmiomana.info&port=666&secret=3emk8jsddowEqNfzkSDKW24=) |
| 19 | `pablo.ps-fifaei.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=pablo.ps-fifaei.ir&port=443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 20 | `91.84.100.213` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.84.100.213&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
