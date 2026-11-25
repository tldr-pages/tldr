# systemctl suspend

> تعلیق سیستم.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#suspend>.

- تعلیق فوری سیستم:

`systemctl suspend`

- زمان‌بندی تعلیق پس از ۵ دقیقه تأخیر:

`sleep 300 && systemctl suspend`

- تعلیق سیستم و سپس خواب زمستانی پس از تأخیر:

`systemctl hybrid-sleep`
