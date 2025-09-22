# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 04:58 31-06-1404)

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
| 1 | `87.229.100.201` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.229.100.201&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `my.usrapid.harcibasheokeyee.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=my.usrapid.harcibasheokeyee.ir&port=443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 3 | `176.9.241.217` | `98` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=176.9.241.217&port=98&secret=eecBAgABAAfwAwOG4kw63QAAAARueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29t) |
| 4 | `140.233.187.31` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=140.233.187.31&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d) |
| 5 | `14.102.10.132` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.132&port=85&secret=ee00ff000fffff00fff5555ffffffffff5662e6b6f2d2d) |
| 6 | `185.21.12.130` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.21.12.130&port=443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `146.190.229.203` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.190.229.203&port=443&secret=ee79e344818749bd7ac519130220c25d09636865636b2d686f73742e6e6574) |
| 8 | `91.84.110.130` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.84.110.130&port=443&secret=7otdyWf9v23L9+j4vrzGtv5OemY0WUxtZGg0T3NCcDUwNUFBMDUwMDEwMjAzMDQwNTA2MDcwODA5Li11cGRhdGUxLmFuZHJvaWQuZ29vZ2xlLnN5bmMuaW1hZ2UudG5hYmlzaWJpemlwLmly) |
| 9 | `new.sitemcinet.co.uk` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=new.sitemcinet.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 10 | `91.98.42.138` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.42.138&port=9443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `5.161.52.236` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=5.161.52.236&port=443&secret=ee1100e547d760f0e3b53eb430c871f1886170706c652e636f6d) |
| 12 | `87.248.132.35` | `170` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.35&port=170&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 13 | `bob.hotelghooo.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=bob.hotelghooo.ir&port=443&secret=ee000000000000000000000000000000007777772e4869646550726f78692e696f) |
| 14 | `sahebe-sabr.nokande.info` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sahebe-sabr.nokande.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 15 | `65.109.191.22` | `300` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=65.109.191.22&port=300&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 16 | `nuke.download-ir.co.uk.` | `6443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=nuke.download-ir.co.uk.&port=6443&secret=eeNEgYdJvXrFGRMCIMJdCQ==) |
| 17 | `4777.ir.koch.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=4777.ir.koch.newdf12.info&port=8888&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 18 | `89.251.10.31` | `6443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.251.10.31&port=6443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d) |
| 19 | `87.aiproxnewdomainio.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.aiproxnewdomainio.info&port=8888&secret=1320PuNyHw_LQKT_Y7XNJw) |
| 20 | `2.e7.ir.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=2.e7.ir.newdf12.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
