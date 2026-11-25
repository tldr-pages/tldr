# rexec

> اجرای دستور در میزبان راه دور.
> توجه: از `rexec` با احتیاط استفاده کنید، زیرا داده‌ها را به‌صورت متن ساده منتقل می‌کند. برای ارتباط رمزگذاری‌شده جایگزین‌های امن مانند SSH را در نظر بگیرید.
> اطلاعات بیشتر: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rexec-invocation>.

- اجرای دستور در میزبان راه دور:

`rexec {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- تعیین نام کاربری راه دور در میزبان راه دور:

`rexec {{[-u|--username]}} {{username}} {{[-h|--host]}} {{remote_host}} {{ps aux}}`

- هدایت `stdin` از `/dev/null` در میزبان راه دور:

`rexec {{[-n|--noerr]}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`

- تعیین پورت راه دور در میزبان راه دور:

`rexec {{[-P|--port]}} {{1234}} {{[-h|--host]}} {{remote_host}} {{ls -l}}`
