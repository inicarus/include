# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 21:54 30-06-1404)

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
| 1 | `app.cdnhub.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.cdnhub.ir&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5iZWVmLmN5YmVyMjRzZWN1cml0eS5kZS5rYXJlbmhvc3QuaXI) |
| 2 | `5.35.38.249` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.35.38.249&port=443&secret=1320PuNyHw_LQKT_Y7XNJw) |
| 3 | `91.98.20.225` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.20.225&port=8888&secret=ee5lrPbFdb1vizwd3HEHowtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 4 | `5.35.33.235` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.35.33.235&port=443&secret=ee1603010200010001fc030386e24c3add646e2e79656b74616e65742e636f6d646c2e676f6f676c652e636f6d666172616B61762E636F6D160301020001000100000000000000000000000000000000) |
| 5 | `2222.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2222.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 6 | `65.21.239.223` | `80` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.21.239.223&port=80&secret=ee1603010200010001fc030386e24c3add646e2e79656b74616e65742e636f6d646c2e676f6f676c652e636f6d666172616b61762e636f6d160301020001000100000000000000000000000000000000) |
| 7 | `195.200.18.147` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.200.18.147&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 8 | `347474.ir.koch.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=347474.ir.koch.newdf12.info&port=8888&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 9 | `147.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=147.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `195.200.19.26` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=195.200.19.26&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 11 | `11.e7.ir.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=11.e7.ir.newdf12.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 12 | `mtproto.online` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=mtproto.online&port=443&secret=ee139e0ee36150c1ea3bf299796586b5457777772e7674622e7275) |
| 13 | `7887769876711.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7887769876711.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 14 | `offer.housing-agency.co.uk` | `9741` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=offer.housing-agency.co.uk&port=9741&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 15 | `45.14.245.128` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.14.245.128&port=443&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 16 | `68.233.124.248` | `1444` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=68.233.124.248&port=1444&secret=ee548593a9c0688f4f7d9d57377897d96473332e616d617a6f6e6177732e636f6d) |
| 17 | `185.157.214.109` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.157.214.109&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 18 | `49.13.145.61` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.13.145.61&port=443&secret=3QAAAAAAAAAAAAAAAAAAAAA=) |
| 19 | `16777771.e7.ir.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=16777771.e7.ir.newdf12.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 20 | `46.4.214.188` | `155` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=46.4.214.188&port=155&secret=eeRighJJvXrFGRMCIMJdCQ) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
