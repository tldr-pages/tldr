# dirbuster

> جست‌وجوی فراگیر دایرکتوری‌ها و نام فایل‌ها روی سرورها.
> اطلاعات بیشتر: <https://www.kali.org/tools/dirbuster/>.

- شروع در حالت رابط گرافیکی:

`dirbuster -u {{http://example.com}}`

- شروع در حالت بدون رابط گرافیکی:

`dirbuster -H -u {{http://example.com}}`

- تنظیم فهرست پسوند فایل‌ها:

`dirbuster -e {{txt,html}}`

- فعال کردن خروجی مفصل:

`dirbuster -v`

- تعیین محل گزارش:

`dirbuster -r {{path/to/report.txt}}`
