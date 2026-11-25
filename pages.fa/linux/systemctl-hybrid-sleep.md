# systemctl hybrid-sleep

> بردن سیستم به خواب ترکیبی که تعلیق در RAM و خواب زمستانی را ترکیب می‌کند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#hybrid-sleep>.

- بردن فوری سیستم به خواب ترکیبی:

`systemctl hybrid-sleep`

- اجبار خواب ترکیبی حتی در صورت وجود ممانعت‌کننده‌ها:

`systemctl hybrid-sleep {{[-f|--force]}}`

- بردن سیستم به خواب ترکیبی بدون ارسال پیام همگانی به کاربران واردشده:

`systemctl hybrid-sleep --no-wall`
