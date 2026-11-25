# rmmod

> حذف ماژول‌ها از هستهٔ لینوکس.
> همچنین : `kmod`.
> اطلاعات بیشتر: <https://manned.org/rmmod>.

- حذف ماژول از هسته:

`sudo rmmod {{module_name}}`

- حذف ماژول از هسته و نمایش اطلاعات مفصل:

`sudo rmmod --verbose {{module_name}}`

- حذف ماژول از هسته و ارسال خطاها به syslog به‌جای `stderr`:

`sudo rmmod --syslog {{module_name}}`

- نمایش راهنما:

`rmmod --help`

- نمایش نسخه:

`rmmod --version`
