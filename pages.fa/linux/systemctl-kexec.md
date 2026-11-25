# systemctl kexec

> راه‌اندازی مجدد سیستم از طریق kexec.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#kexec>.

- راه‌اندازی مجدد سریع با kexec (اگر هسته از پیش بارگذاری شده باشد):

`systemctl kexec`

- اجبار راه‌اندازی مجدد عادی حتی در صورت وجود kexec:

`systemctl kexec {{[-f|--force]}}`
