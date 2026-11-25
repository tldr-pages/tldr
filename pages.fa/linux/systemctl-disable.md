# systemctl disable

> غیرفعال کردن سرویس‌های systemd.
> همچنین ببینید: `systemctl revert`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#disable%20UNIT%E2%80%A6>.

- جلوگیری از اجرای سرویس هنگام راه‌اندازی:

`systemctl disable {{unit}}`

- جلوگیری از اجرای سرویس هنگام راه‌اندازی و توقف اجرای فعلی آن:

`systemctl disable {{unit}} --now`

- جلوگیری از اجرای سرویس کاربر هنگام ورود:

`systemctl disable {{unit}} --user`
