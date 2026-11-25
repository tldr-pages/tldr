# znc

> واسط پایدار IRC (bouncer).
> اطلاعات بیشتر: <https://manned.org/znc>.

- اجرای تنظیم اولیه:

`znc {{[-c|--makeconf]}}`

- شروع سرویس واسط IRC:

`znc`

- تنظیم `znc` برای systemd:

`sudo {{[-u|--user]}} znc znc {{[-c|--makeconf]}} {{[-d|--datadir]}} /var/lib/znc`

- فعال کردن `znc` برای شروع هنگام راه‌اندازی و شروع فوری آن:

`systemctl enable znc --now`
