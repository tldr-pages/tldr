# systemctl try-restart

> راه‌اندازی مجدد یک یا چند واحد فقط در صورت اجرای فعلی آن‌ها.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#try-restart%20PATTERN%E2%80%A6>.

- راه‌اندازی مجدد واحد مشخص در صورت اجرا:

`systemctl try-restart {{unit}}`

- راه‌اندازی مجدد چند واحد در صورت اجرا:

`systemctl try-restart {{unit1 unit2 ...}}`

- راه‌اندازی مجدد همهٔ واحدهای مطابق الگو در صورت اجرا:

`systemctl try-restart '{{pattern}}'`
