# systemctl list-timers

> فهرست کردن همهٔ زمان‌سنج‌های فعال systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-timers%20PATTERN%E2%80%A6>.

- فهرست کردن همهٔ زمان‌سنج‌های فعال:

`systemctl list-timers`

- فهرست کردن همهٔ زمان‌سنج‌ها، از جمله موارد غیرفعال:

`systemctl list-timers {{[-a|--all]}}`

- فهرست کردن زمان‌سنج‌های مطابق الگو:

`systemctl list-timers {{pattern}}`

- فهرست کردن زمان‌سنج‌های مطابق وضعیت مشخص:

`systemctl list-timers --state {{active|inactive|failed|...}}`
