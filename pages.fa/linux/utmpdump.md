# utmpdump

> چاپ و بارگذاری فایل‌های حسابداری btmp، utmp و wtmp.
> اطلاعات بیشتر: <https://manned.org/utmpdump>.

- چاپ فایل `/var/log/wtmp` در `stdout` به‌صورت متن ساده:

`utmpdump {{/var/log/wtmp}}`

- بارگذاری فایل قبلاً چاپ‌شده در `/var/log/wtmp`:

`utmpdump {{[-r|--reverse]}} {{dumpfile}} >{{/var/log/wtmp}}`
