# systemctl is-system-running

> بررسی وضعیت فعلی سیستم.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-system-running>.

- بررسی عملیاتی بودن سیستم و چاپ وضعیت فعلی:

`systemctl is-system-running`

- بررسی وضعیت فعلی به‌صورت بی‌صدا (بدون خروجی، فقط وضعیت خروج):

`systemctl is-system-running {{[-q|--quiet]}}`

- انتظار برای تکمیل فرایند راه‌اندازی پیش از چاپ وضعیت فعلی:

`systemctl is-system-running --wait`
