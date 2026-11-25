# systemctl list-sockets

> فهرست کردن واحدهای سوکت فعال موجود در حافظه، مرتب‌شده بر اساس آدرس گوش دادن.
> همچنین : `systemctl list-units`, `systemctl list-unit-files`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-sockets%20PATTERN%E2%80%A6>.

- فهرست کردن واحدهای سوکت فعال موجود در حافظه:

`systemctl list-sockets`

- فهرست کردن واحدهای سوکت فعال همراه با نوع سوکت:

`systemctl list-sockets --show-types`

- فهرست کردن همهٔ واحدهای سوکت، از جمله موارد غیرفعال و شکست‌خورده:

`systemctl list-sockets {{[-a|--all]}}`

- فهرست کردن واحدهای سوکت فیلترشده بر اساس وضعیت:

`systemctl list-sockets --state {{active|inactive|failed|...}}`

- فهرست کردن واحدهای سوکت مطابق الگوی نام:

`systemctl list-sockets {{pattern1 pattern2 ...}}`
