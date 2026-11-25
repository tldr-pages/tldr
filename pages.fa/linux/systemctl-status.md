# systemctl status

> نمایش وضعیت واحدهای systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#status%20PATTERN%E2%80%A6%7CPID%E2%80%A6%5D>.

- نمایش وضعیت واحد systemd:

`systemctl status {{unit}}.{{service|timer|socket|target|...}}`

- نمایش وضعیت واحدهای شکست‌خورده:

`systemctl status --failed`

- فهرست کردن همهٔ سرویس‌های در حال اجرا:

`systemctl status`

- فهرست کردن همهٔ واحدهای سیستم:

`systemctl status {{[-a|--all]}}`

- فهرست کردن همهٔ واحدهای نوع مشخص:

`systemctl status {{[-t|--type]}} {{service|timer|socket|target|...}}`

- فهرست کردن همهٔ واحدهای با وضعیت مشخص:

`systemctl status --state {{active|inactive|failed}}`

- نمایش وضعیت واحد کاربر:

`systemctl status {{unit}} --user`
