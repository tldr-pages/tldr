# systemctl exit

> درخواست خروج از مدیر سرویس.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#exit%20EXIT_CODE>.

- خروج از مدیر سرویس کاربر:

`systemctl exit --user`

- خروج از مدیر سرویس کاربر با کد خروج مشخص:

`systemctl exit {{code}} --user`

- درخواست خروج از مدیر سرویس کانتینر (در خارج از کانتینر معادل `systemctl poweroff`):

`systemctl exit`
