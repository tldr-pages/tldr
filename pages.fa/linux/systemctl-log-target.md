# systemctl log-target

> دریافت یا تنظیم مقصد گزارش مدیر systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#log-target%20%5BTARGET%5D>.

- نمایش مقصد گزارش فعلی مدیر systemd:

`systemctl log-target`

- تنظیم مقصد گزارش مدیر:

`systemctl log-target {{journal-or-kmsg|journal|kmsg|console|syslog|null|auto}}`
