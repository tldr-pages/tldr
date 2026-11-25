# systemctl service-log-level

> دریافت یا تنظیم سطح گزارش زمان اجرای سرویس از طریق D-Bus.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#service-log-level%20SERVICE%20%5BLEVEL%5D>.

- نمایش سطح گزارش فعلی سرویس:

`systemctl service-log-level {{service_name}}`

- تنظیم سطح گزارش سرویس (نام سطح را می‌توان با عدد ۰ تا ۷ جایگزین کرد):

`systemctl service-log-level {{service_name}} {{emerg|alert|crit|err|warning|notice|info|debug}}`
