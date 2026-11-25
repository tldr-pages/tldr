# systemctl service-log-target

> دریافت یا تنظیم مقصد گزارش سرویس.
> فقط برای سرویس‌های یکپارچه با D-Bus کار می‌کند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#service-log-target%20SERVICE%20%5BTARGET%5D>.

- نمایش مقصد گزارش فعلی سرویس:

`systemctl service-log-target {{service_name}}`

- تنظیم مقصد گزارش به `console` (ارسال گزارش‌ها به `stderr`):

`systemctl service-log-target {{service_name}} console`

- تنظیم مقصد گزارش به `journal` (ارسال گزارش‌ها به `systemd-journald`):

`systemctl service-log-target {{service_name}} journal`

- تنظیم مقصد گزارش به `syslog` (ارسال گزارش‌ها به `/dev/log`):

`systemctl service-log-target {{service_name}} syslog`

- اجازه به systemd برای انتخاب مقصد گزارش مناسب:

`systemctl service-log-target {{service_name}} auto`

- غیرفعال کردن همهٔ خروجی گزارش:

`systemctl service-log-target {{service_name}} null`
