# logrotate

> چرخش، فشرده‌سازی و ارسال گزارش‌های سیستم با ایمیل.
> اطلاعات بیشتر: <https://manned.org/logrotate>.

- اجرای دستی:

`logrotate {{path/to/logrotate.conf}} --force`

- اجرا با دستور مشخص برای ارسال گزارش‌ها:

`logrotate {{path/to/logrotate.conf}} --mail {{/usr/bin/mail_command}}`

- اجرا بدون استفاده از فایل وضعیت (قفل):

`logrotate {{path/to/logrotate.conf}} --state /dev/null`

- اجرا و صرف‌نظر از بررسی فایل وضعیت (قفل):

`logrotate {{path/to/logrotate.conf}} --skip-state-lock`

- تنظیم `logrotate` برای ثبت خروجی مفصل در فایل گزارش:

`logrotate {{path/to/logrotate.conf}} --log {{path/to/log_file}}`
