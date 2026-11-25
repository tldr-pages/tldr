# loginctl

> مدیریت مدیر ورود systemd.
> همچنین ببینید: `lslogins`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/loginctl.html>.

- چاپ همهٔ نشست‌های فعلی:

`loginctl`

- چاپ همهٔ ویژگی‌های نشست مشخص:

`loginctl show-session {{session_id}} {{[-a|--all]}}`

- چاپ همهٔ ویژگی‌های کاربر مشخص:

`loginctl show-user {{username}}`

- چاپ ویژگی مشخصی از کاربر:

`loginctl show-user {{username}} {{[-p|--property]}} {{property_name}}`

- اجرای عملیات `loginctl` در میزبان راه دور:

`loginctl list-users {{[-H|--host]}} {{hostname}}`

- خارج کردن کاربر از همهٔ نشست‌های او:

`loginctl terminate-user {{username}}`

- نمایش راهنما:

`loginctl {{[-h|--help]}}`
