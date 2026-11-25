# sslstrip

> انجام حملات حذف SSL متعلق به Moxie Marlinspike.
> هم‌زمان حملهٔ جعل ARP انجام دهید.
> اطلاعات بیشتر: <https://www.kali.org/tools/sslstrip/>.

- ثبت فقط ترافیک HTTPS POST روی پورت پیش‌فرض ۱۰۰۰۰:

`sslstrip`

- ثبت فقط ترافیک HTTPS POST روی پورت ۸۰۸۰:

`sslstrip --listen=8080`

- ثبت همهٔ ترافیک SSL ورودی و خروجی سرور روی پورت ۸۰۸۰:

`sslstrip --ssl --listen=8080`

- ثبت همهٔ ترافیک SSL و HTTP ورودی و خروجی سرور روی پورت ۸۰۸۰:

`sslstrip --listen=8080 --all`

- تعیین مسیر فایل ذخیرهٔ گزارش‌ها:

`sslstrip --listen={{8080}} --write={{path/to/file}}`

- نمایش راهنما:

`sslstrip --help`
