# restorecond

> سرویسی که ایجاد فایل را پایش و زمینه‌های SELinux را خودکار بازیابی می‌کند.
> برای دایرکتوری‌هایی که فایل‌ها اغلب با زمینهٔ نادرست ایجاد می‌شوند مفید است.
> همچنین : `restorecon`, `semanage fcontext`.
> اطلاعات بیشتر: <https://manned.org/restorecond>.

- شروع سرویس `restorecond`:

`sudo restorecond`

- اجرای `restorecond` در حالت مفصل برای مشاهدهٔ رویدادهای بازیابی:

`sudo restorecond -v`

- اجرای `restorecond` در حالت اشکال‌زدایی:

`sudo restorecond -d`

- استفاده از فایل جایگزین `restorecond.conf`:

`sudo restorecond -f restorecond_file`

- بررسی وضعیت سرویس restorecond:

`sudo systemctl status restorecond`

- فعال کردن restorecond برای شروع هنگام راه‌اندازی:

`sudo systemctl enable restorecond --now`
