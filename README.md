# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 14:53 30-06-1404)

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
| 1 | `89.110.111.195` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.110.111.195&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 2 | `195.62.32.99` | `9861` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.62.32.99&port=9861&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 3 | `48483.meli.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=48483.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 4 | `7.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | `117108899.meli.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=117108899.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | `91.238.92.176` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.238.92.176&port=443&secret=7otdyWf9v23L9-j4vrzGtv5OemY0WUxtZGg0T3NCcDUwNUFBMDUwMDEwMjAzMDQwNTA2MDcwODA5Li11cGRhdGUxLmFuZHJvaWQuZ29vZ2xlLnN5bmMuaW1hZ2UudG5hYmlzaWJpemlwLmly) |
| 7 | `103.161.34.251` | `9861` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=103.161.34.251&port=9861&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 8 | `brookswashere.space` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=brookswashere.space&port=443&secret=10dadd1e7c27a20098abb5bf53ca26a8) |
| 9 | `91.98.39.91` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.39.91&port=9443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 10 | `140.233.167.20` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=140.233.167.20&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `89.251.10.24` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.251.10.24&port=443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d) |
| 12 | `qavi.189-208-55-72.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=qavi.189-208-55-72.ir&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 13 | `77.238.239.178` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=77.238.239.178&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 14 | `91.99.182.228` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.182.228&port=9443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 15 | `88.80.139.140` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=88.80.139.140&port=443&secret=7777772e6e69632e69727w) |
| 16 | `austria.salzburg.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=austria.salzburg.ir&port=443&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D) |
| 17 | `9933.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=9933.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 18 | `op.hotelghooo.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=op.hotelghooo.ir&port=443&secret=ee000000000000000000000000000000007777772e4869646550726f78692e696f) |
| 19 | `enable-rquest-security-support.allow-reuest.co.uk` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=enable-rquest-security-support.allow-reuest.co.uk&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d) |
| 20 | `yaho.koptrin.48.37-68-174.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=yaho.koptrin.48.37-68-174.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
