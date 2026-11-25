# systemctl list-unit-files

> فهرست کردن فایل‌های واحد نصب‌شده و وضعیت فعال‌سازی آن‌ها.
> همچنین : `systemctl list-units`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-unit-files%20PATTERN%E2%80%A6>.

- فهرست کردن فایل‌های واحد نصب‌شده و وضعیت آن‌ها:

`systemctl list-unit-files`

- فیلتر بر اساس وضعیت:

`systemctl list-unit-files --state {{enabled|disabled|static|...}}`

- فیلتر بر اساس نوع واحد:

`systemctl list-unit-files {{[-t|--type]}} {{service|socket|timer|...}}`

- فیلتر بر اساس الگوی نام:

`systemctl list-unit-files '{{sshd*}}'`

- چاپ مستقیم خروجی در `stdout`:

`systemctl list-unit-files --no-pager`

- چاپ خروجی بدون سربرگ یا پانوشت:

`systemctl list-unit-files --no-legend`
