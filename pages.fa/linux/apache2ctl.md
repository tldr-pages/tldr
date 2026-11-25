# apache2ctl

> مدیریت وب‌سرور HTTP آپاچی.
> این دستور همراه سیستم‌عامل‌های مبتنی بر دبیان ارائه می‌شود؛ برای سیستم‌های مبتنی بر RHEL، دستور `httpd` را ببینید.
> اطلاعات بیشتر: <https://manned.org/apache2ctl>.

- شروع سرویس آپاچی؛ اگر در حال اجرا باشد پیامی نمایش می‌دهد:

`sudo apache2ctl start`

- توقف سرویس آپاچی:

`sudo apache2ctl stop`

- راه‌اندازی مجدد سرویس آپاچی:

`sudo apache2ctl restart`

- بررسی نحو فایل پیکربندی:

`sudo apache2ctl -t`

- فهرست کردن ماژول‌های بارگذاری‌شده:

`sudo apache2ctl -M`
