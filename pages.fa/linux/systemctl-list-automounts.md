# systemctl list-automounts

> فهرست کردن واحدهای اتصال خودکار موجود در حافظه، همراه با مسیرهای اتصال و نام واحدها.
> همچنین : `systemctl list-units`, `systemctl list-unit-files`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#list-automounts%20PATTERN%E2%80%A6>.

- فهرست کردن واحدهای اتصال خودکار موجود در حافظه:

`systemctl list-automounts`

- فهرست کردن همهٔ واحدهای اتصال خودکار، از جمله موارد غیرفعال:

`systemctl list-automounts {{[-a|--all]}}`

- فیلتر واحدهای اتصال خودکار بر اساس وضعیت:

`systemctl list-automounts --state {{active|inactive|failed|...}}`

- فیلتر واحدهای اتصال خودکار بر اساس الگوی نام:

`systemctl list-automounts {{pattern1 pattern2 ...}}`
