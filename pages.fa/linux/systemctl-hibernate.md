# systemctl hibernate

> بردن سیستم به خواب زمستانی با ذخیرهٔ وضعیت فعلی روی دیسک و خاموش کردن.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#hibernate>.

- بردن فوری سیستم به خواب زمستانی:

`systemctl hibernate`

- اجبار خواب زمستانی حتی در صورت وجود ممانعت‌کننده‌ها:

`systemctl hibernate {{[-f|--force]}}`

- بردن سیستم به خواب زمستانی بدون ارسال پیام به کاربران واردشده:

`systemctl hibernate --no-wall`
