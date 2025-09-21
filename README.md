# 📊 Khoda Proxy Finder (آخرین بروزرسانی: 14:29 30-06-1404)

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
| 1 | `117.55.202.82` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=117.55.202.82&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 2 | `9911.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=9911.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 3 | `93.183.88.188` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=93.183.88.188&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 4 | `033636737377377.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=033636737377377.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 5 | `163.5.31.77` | `8443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=163.5.31.77&port=8443&secret=EERighJJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 6 | `49.13.220.199` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=49.13.220.199&port=9443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 7 | `6.meli.meli.zban-mas.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=6.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 8 | `140.238.11.149` | `11443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=140.238.11.149&port=11443&secret=ee548593a9c0688f4f7d9d57377897d96473332e616d617a6f6e6177732e636f6d) |
| 9 | `91.98.81.108` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.98.81.108&port=9443&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 10 | `185.21.15.140` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.21.15.140&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQRueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 11 | `soraat.bala.polparast.ir` | `231` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=soraat.bala.polparast.ir&port=231&secret=ee5lrPbFdb1vizwd3HEHowtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA) |
| 12 | `14.102.10.50` | `888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=14.102.10.50&port=888&secret=FgMBAgABAAH8AwOG4kw63Q) |
| 13 | `185.21.14.158` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=185.21.14.158&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D) |
| 14 | `75127.e7.ir.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=75127.e7.ir.newdf12.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 15 | `op.hotelghooo.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=op.hotelghooo.ir&port=443&secret=ee000000000000000000000000000000007777772e4869646550726f78692e696f) |
| 16 | `app.cdnhub.ir` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=app.cdnhub.ir&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5iZWVmLmN5YmVyMjRzZWN1cml0eS5kZS5rYXJlbmhvc3QuaXI) |
| 17 | `89.251.10.3` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=89.251.10.3&port=443&secret=ee151151151151151151151151151151156d656469612e737465616d706f77657265642e636f6d) |
| 18 | `91.99.183.122` | `443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=91.99.183.122&port=443&secret=eec862057ba49a7ecdf0ad4eb44cd5bb11646f776e6c6f61642e77696e646f77737570646174652e636f6d) |
| 19 | `777571277.e7.ir.newdf12.info` | `8888` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=777571277.e7.ir.newdf12.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t) |
| 20 | `45.76.184.13` | `9443` | ✅ فعال | [لینک پروکسی](https://t.me/proxy?server=45.76.184.13&port=9443&secret=2adab36179e7a39026adf74034615248) |

> **💡 نکته**: این جدول فقط نمونه‌ای از پروکسی‌هاست. برای دسترسی به لیست کامل و به‌روز، فایل [proxy.txt](proxy.txt) را دانلود کنید یا از **[صفحه وب پروژه](https://inicarus.github.io/khoda/)** استفاده کنید.

## 🤝 مشارکت
از ایده‌ها و مشارکت شما استقبال می‌کنیم! برای بهبود پروژه:
1. یک **Issue** در مخزن باز کنید.
2. یا یک **Pull Request** با تغییرات پیشنهادی ارسال کنید.

## 📜 لایسنس
این پروژه تحت [لایسنس MIT](LISENSE) منتشر شده است.
