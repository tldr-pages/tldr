# systemctl reload-or-restart

> بارگذاری مجدد واحدهای `systemd` یا در غیر این صورت راه‌اندازی مجدد آن‌ها.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#reload-or-restart%20PATTERN%E2%80%A6>.

- بارگذاری مجدد یا راه‌اندازی مجدد واحد:

`systemctl reload-or-restart {{unit}}`

- بارگذاری مجدد یا راه‌اندازی مجدد چند واحد مطابق الگو:

`systemctl reload-or-restart {{pattern}}`

- اجرای دستور بدون انتظار برای تکمیل عملیات:

`systemctl reload-or-restart {{unit}} --no-block`

- اعمال دستور فقط به واحدهای کاربر:

`systemctl reload-or-restart {{unit}} --user`
