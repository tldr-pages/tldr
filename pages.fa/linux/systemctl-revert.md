# systemctl revert

> بازگرداندن فایل‌های واحد به نسخه‌های سازنده.
> اثرات `edit`، `enable`، `disable`، `set-property` و `mask` را برمی‌گرداند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#revert%20UNIT%E2%80%A6>.

- بازگرداندن فایل‌های واحد به تنظیمات پیش‌فرض:

`systemctl revert {{unit1 unit2 ...}}`

- بازگرداندن فایل واحد کاربر:

`systemctl revert {{unit}} --user`
