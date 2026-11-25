# systemctl enable

> فعال کردن سرویس‌های systemd.
> همچنین ببینید: `systemctl revert`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#enable%20UNIT%E2%80%A6>.

- فعال کردن سرویس برای اجرا هنگام راه‌اندازی:

`systemctl enable {{unit}}`

- فعال کردن سرویس برای اجرا هنگام راه‌اندازی و شروع فوری آن:

`systemctl enable {{unit}} --now`

- فعال کردن واحد کاربر برای اجرا هنگام ورود:

`systemctl enable {{unit}} --user`
