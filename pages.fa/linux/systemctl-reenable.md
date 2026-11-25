# systemctl reenable

> فعال‌سازی مجدد یک یا چند واحد.
> هنگام تغییر هدف‌های سرویس استفاده می‌شود.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reenable%20UNIT%E2%80%A6>.

- فعال‌سازی مجدد واحد و بازیابی پیوندهای نمادین پیش‌فرض آن:

`systemctl reenable {{unit}}`

- فعال‌سازی مجدد چند واحد هم‌زمان:

`systemctl reenable {{unit1 unit2 ...}}`

- فعال‌سازی مجدد واحد و شروع فوری آن:

`systemctl reenable {{unit}} --now`
