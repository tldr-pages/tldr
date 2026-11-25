# getsebool

> دریافت مقدار بولی SELinux.
> همچنین ببینید: `semanage boolean`, `setsebool`.
> اطلاعات بیشتر: <https://manned.org/getsebool>.

- نمایش تنظیم فعلی یک مقدار بولی:

`getsebool {{httpd_can_connect_ftp}}`

- نمایش تنظیم فعلی همهٔ مقادیر بولی با `-a`:

`getsebool -a`

- نمایش تنظیم فعلی همهٔ مقادیر بولی همراه با توضیحات:

`sudo semanage boolean {{[-l|--list]}}`
