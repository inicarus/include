# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 14:04 30-06-1404)

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
| 1 | `www.doevoee.co.uk` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=www.doevoee.co.uk&port=8888&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `49.13.145.67` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.13.145.67&port=443&secret=3QAAAAAAAAAAAAAAAAAAAAA=) |
| 3 | `6679788288733.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6679788288733.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 4 | `87.248.132.38` | `85` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.38&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D) |
| 5 | `7377374.Ir.koch.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7377374.Ir.koch.newdf12.info&port=8888&secret=1320PuNyHw_LQKT_Y7XNJw==) |
| 6 | `sariee.45.712.38-82.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sariee.45.712.38-82.ir&port=443&secret=7hBKyBmZ41cUX4K5nIpow3ltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 7 | `87.248.132.188` | `200` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.132.188&port=200&secret=ee0000f00f0f775555fffffff5006e2e69646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 8 | `146.103.120.48` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.120.48&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 9 | `14.102.10.154` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.154&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 10 | `sadra.mygrade.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=sadra.mygrade.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 11 | `000099772.df.ir.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=000099772.df.ir.newdf12.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 12 | `146.103.113.100` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.113.100&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 13 | `14.102.10.18` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.18&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ) |
| 14 | `giahi-vegeterian.khunebagh.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=giahi-vegeterian.khunebagh.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d) |
| 15 | `144.124.229.192` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=144.124.229.192&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFy) |
| 16 | `7443.iropt-g.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=7443.iropt-g.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 17 | `87.248.134.66` | `200` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=87.248.134.66&port=200&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 18 | `146.103.109.37` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=146.103.109.37&port=443&secret=eeDDNEgYdJvXrFGRMCIMJQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 19 | `185.245.104.241` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.245.104.241&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 20 | `noise.sibiu.ir` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=noise.sibiu.ir&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
