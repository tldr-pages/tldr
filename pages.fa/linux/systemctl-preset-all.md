# systemctl preset-all

> بازنشانی وضعیت فعال‌سازی همهٔ واحدهای نصب‌شده به مقادیر پیش‌فرض مشخص‌شده در فایل‌های سیاست پیش‌تنظیم.
> همچنین : `systemctl preset`, `systemctl list-unit-files`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#preset-all>.

- بازنشانی وضعیت فعال‌سازی همهٔ واحدهای نصب‌شده:

`sudo systemctl preset-all`

- فعال کردن فقط در صورت علامت‌گذاری به‌عنوان فعال در سیاست پیش‌تنظیم:

`sudo systemctl preset-all --preset-mode enable-only`

- غیرفعال کردن فقط در صورت علامت‌گذاری به‌عنوان غیرفعال در سیاست پیش‌تنظیم:

`sudo systemctl preset-all --preset-mode disable-only`

- عدم نمایش خروجی و بازگرداندن فقط کد خروج:

`sudo systemctl preset-all {{[-q|--quiet]}}`
