# systemctl link

> پیوند دادن فایل واحد خارج از مسیر جست‌وجوی فایل واحد به مسیر جست‌وجو.
> همچنین : `systemctl disable`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#link%20PATH%E2%80%A6>.

- پیوند دادن فایل واحد برای در دسترس قرار دادن آن برای دستورهای systemd:

`systemctl link {{path/to/service}}`

- پیوند دادن چند فایل واحد هم‌زمان:

`systemctl link {{path/to/service1 path/to/service2 ...}}`
