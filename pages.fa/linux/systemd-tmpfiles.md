# systemd-tmpfiles

> ایجاد، حذف و پاک‌سازی فایل‌ها و دایرکتوری‌های موقت و ناپایدار.
> این دستور هنگام راه‌اندازی توسط سرویس‌های systemd خودکار فراخوانی می‌شود و معمولاً اجرای دستی لازم نیست.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-tmpfiles.html>.

- ایجاد فایل‌ها و دایرکتوری‌ها مطابق پیکربندی:

`sudo systemd-tmpfiles --create`

- ایجاد فایل‌ها و دایرکتوری‌های مطابق فقط پیشوند مسیر مشخص:

`sudo systemd-tmpfiles --create --prefix {{/var/log/journal}}`

- پاک‌سازی فایل‌ها و دایرکتوری‌های دارای پارامتر سن پیکربندی‌شده:

`sudo systemd-tmpfiles --clean`

- حذف فایل‌ها و دایرکتوری‌ها مطابق پیکربندی:

`sudo systemd-tmpfiles --remove`

- اعمال عملیات برای پیکربندی‌های مختص کاربر:

`sudo systemd-tmpfiles --create --user`

- اجرای خطوط علامت‌گذاری‌شده برای ابتدای راه‌اندازی:

`sudo systemd-tmpfiles --create --boot`
