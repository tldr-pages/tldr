# systemctl try-reload-or-restart

> بارگذاری مجدد یک یا چند واحد در صورت پشتیبانی، در غیر این صورت راه‌اندازی مجدد آن‌ها.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#try-reload-or-restart%20PATTERN%E2%80%A6>.

- بارگذاری مجدد یا راه‌اندازی مجدد واحد مشخص:

`systemctl try-reload-or-restart {{unit}}`

- بارگذاری مجدد یا راه‌اندازی مجدد چند واحد:

`systemctl try-reload-or-restart {{unit1 unit2 ...}}`

- بارگذاری مجدد یا راه‌اندازی مجدد همهٔ واحدهای مطابق الگو:

`systemctl try-reload-or-restart '{{pattern}}'`
