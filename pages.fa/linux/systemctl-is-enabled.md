# systemctl is-enabled

> بررسی فعال بودن فایل‌های واحد.
> همچنین ببینید: `systemctl enable`, `systemctl disable`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-enabled%20UNIT%E2%80%A6>.

- نمایش وضعیت فعال‌سازی:

`systemctl is-enabled {{unit1 unit2 ...}}`

- عدم نمایش خروجی و بازگرداندن فقط کد خروج:

`systemctl is-enabled {{unit}} {{[-q|--quiet]}}`

- نمایش هدف‌های نصب و مسیرهای پیوند نمادین:

`systemctl is-enabled {{unit}} {{[-l|--full]}}`
