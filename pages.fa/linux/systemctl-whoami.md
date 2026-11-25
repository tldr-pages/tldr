# systemctl whoami

> نمایش واحدهای متعلق به فرایندها.
> اگر PID مشخص نشود، واحدی را نشان می‌دهد که دستور `systemctl` در آن فراخوانی شده است.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#whoami%20%5BPID%E2%80%A6%5D>.

- نمایش واحد پوستهٔ فعلی (محل اجرای `systemctl`):

`systemctl whoami`

- نمایش واحد پوستهٔ فعلی در مدیر سرویس کاربر (سرویس‌های مدیریت‌شده برای نشست ورود):

`systemctl whoami --user`

- نمایش واحد متعلق به فرایند مشخص:

`systemctl whoami {{process_id}}`

- نمایش واحدهای چند فرایند:

`systemctl whoami {{process_id1 process_id2 ...}}`
