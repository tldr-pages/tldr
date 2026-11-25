# systemctl-poweroff

> خاموش کردن سیستم.
> همچنین ببینید: `poweroff`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#poweroff>.

- خاموش کردن سیستم:

`systemctl poweroff`

- خاموش کردن فوری سیستم بدون درخواست توقف صحیح از سرویس‌ها:

`systemctl poweroff {{[-f|--force]}}`

- خاموش کردن فوری سیستم بدون ارسال اعلان به کاربران واردشده:

`systemctl poweroff {{[-f|--force]}} --no-wall`
