# systemctl

> کنترل مدیر سیستم و سرویس systemd.
> برخی زیردستورها مانند `disable`، `status` و `reboot` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html>.

- نمایش همهٔ سرویس‌های در حال اجرا:

`systemctl status`

- فهرست کردن واحدهای شکست‌خورده:

`systemctl --failed`

- شروع، توقف، راه‌اندازی مجدد، بارگذاری مجدد یا نمایش وضعیت سرویس:

`systemctl {{start|stop|restart|reload|status}} {{unit}}`

- فعال یا غیرفعال کردن واحد برای شروع هنگام راه‌اندازی:

`systemctl {{enable|disable}} {{unit}}`

- بارگذاری مجدد systemd و پویش واحدهای جدید یا تغییرکرده:

`systemctl daemon-reload`

- بررسی فعال، فعال‌شده یا شکست‌خورده بودن واحد:

`systemctl {{is-active|is-enabled|is-failed}} {{unit}}`

- فهرست کردن همهٔ واحدهای سرویس، سوکت یا اتصال خودکار با فیلتر وضعیت در حال اجرا یا شکست‌خورده:

`systemctl list-units {{[-t|--type]}} {{service|socket|automount|...}} --state {{failed|running}}`

- نمایش محتوا و مسیر مطلق فایل واحد یا ویرایش آن:

`systemctl {{cat|edit}} {{unit}}`
