# systemctl reload

> بارگذاری مجدد پیکربندی سرویس بدون راه‌اندازی مجدد آن.
> این کار خود سرویس را بارگذاری مجدد می‌کند (مانند پیکربندی Apache یا `nginx`)، نه فایل واحد systemd را.
> برای بارگذاری مجدد فایل‌های واحد از `systemctl daemon-reload` استفاده کنید.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reload%20PATTERN%E2%80%A6>.

- بارگذاری مجدد سرویس:

`systemctl reload {{nginx}}`

- بارگذاری مجدد چند سرویس:

`systemctl reload {{unit1 unit2 ...}}`

- بارگذاری مجدد سرویس برای کاربر فعلی:

`systemctl reload {{pipewire}} --user`
