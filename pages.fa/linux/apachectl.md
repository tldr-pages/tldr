# apachectl

> کنترل وب‌سرور HTTP آپاچی.
> اطلاعات بیشتر: <https://manned.org/apachectl>.

- شروع سرور:

`sudo apachectl start`

- راه‌اندازی مجدد سرور:

`sudo apachectl restart`

- توقف سرور:

`sudo apachectl stop`

- بررسی اعتبار فایل پیکربندی:

`apachectl configtest`

- بررسی وضعیت سرور (به مرورگر lynx نیاز دارد):

`apachectl status`

- بارگذاری مجدد پیکربندی بدون قطع اتصال‌ها:

`sudo apachectl graceful`

- چاپ پیکربندی کامل آپاچی (همیشه پشتیبانی نمی‌شود):

`apachectl -S`

- نمایش راهنما:

`apachectl -h`
