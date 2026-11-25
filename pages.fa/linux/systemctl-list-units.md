# systemctl list-units

> فهرست کردن واحدهایی که systemd اکنون در حافظه دارد.
> همچنین ببینید: `systemctl list-unit-files`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-units%20PATTERN%E2%80%A6>.

- فهرست کردن واحدهای فعال، دارای کار در انتظار یا شکست‌خورده:

`systemctl list-units`

- فهرست کردن همهٔ واحدها، از جمله موارد غیرفعال:

`systemctl list-units {{[-a|--all]}}`

- فیلتر بر اساس نوع واحد:

`systemctl list-units {{[-t|--type]}} {{service|socket|timer|...}}`

- فیلتر بر اساس وضعیت:

`systemctl list-units --state {{running|listening|dead|...}}`

- فیلتر بر اساس الگوی نام:

`systemctl list-units 'systemd*'`

- چاپ مستقیم خروجی در `stdout`:

`systemctl list-units --no-pager`

- چاپ خروجی بدون سربرگ یا پانوشت (برای اسکریپت‌ها):

`systemctl list-units --no-legend`
