# rsh

> اجرای دستورها در میزبان راه دور.
> اطلاعات بیشتر: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rsh-invocation>.

- اجرای دستور در میزبان راه دور:

`rsh {{remote_host}} {{ls -l}}`

- اجرای دستور در میزبان راه دور با نام کاربری مشخص:

`rsh {{remote_host}} {{[-l|--user]}} {{username}} {{ls -l}}`

- هدایت `stdin` به `/dev/null` هنگام اجرای دستور در میزبان راه دور:

`rsh {{remote_host}} --no-err {{ls -l}}`
