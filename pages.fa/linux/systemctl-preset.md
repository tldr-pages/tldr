# systemctl preset

> بازنشانی وضعیت فعال‌سازی فایل‌های واحد به مقادیر پیش‌فرض مشخص‌شده در فایل‌های سیاست پیش‌تنظیم.
> همچنین ببینید: `systemctl preset-all`, `systemctl list-unit-files`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#preset%20UNIT%E2%80%A6>.

- بازنشانی وضعیت فعال‌سازی به پیش‌فرض‌های پیش‌تنظیم:

`systemctl preset {{unit1 unit2 ...}}`

- فعال کردن فقط در صورت علامت‌گذاری به‌عنوان فعال در سیاست پیش‌تنظیم:

`systemctl preset {{unit}} --preset-mode enable-only`

- غیرفعال کردن فقط در صورت علامت‌گذاری به‌عنوان غیرفعال در سیاست پیش‌تنظیم:

`systemctl preset {{unit}} --preset-mode disable-only`

- عدم نمایش خروجی و بازگرداندن فقط کد خروج:

`systemctl preset {{unit}} {{[-q|--quiet]}}`
