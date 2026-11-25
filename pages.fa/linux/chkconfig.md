# chkconfig

> مدیریت سطح اجرای سرویس‌ها در CentOS 6.
> اطلاعات بیشتر: <https://manned.org/chkconfig>.

- فهرست کردن سرویس‌ها همراه با سطح اجرا:

`chkconfig --list`

- نمایش سطح اجرای یک سرویس:

`chkconfig --list {{ntpd}}`

- فعال کردن سرویس هنگام راه‌اندازی:

`chkconfig {{sshd}} on`

- فعال کردن سرویس هنگام راه‌اندازی برای سطوح اجرای ۲، ۳، ۴ و ۵:

`chkconfig --level 2345 {{sshd}} on`

- غیرفعال کردن سرویس هنگام راه‌اندازی:

`chkconfig {{ntpd}} off`

- غیرفعال کردن سرویس هنگام راه‌اندازی برای سطح اجرای ۳:

`chkconfig --level 3 {{ntpd}} off`
