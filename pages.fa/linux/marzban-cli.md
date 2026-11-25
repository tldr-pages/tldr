# marzban cli

> مدیریت مدیران، کاربران و اشتراک‌ها.
> اطلاعات بیشتر: <https://github.com/Gozargah/Marzban/blob/master/cli/README.md>.

- فهرست کردن همهٔ مدیران:

`marzban cli admin list`

- ایجاد مدیر جدید:

`marzban cli admin create {{[-u|--username]}} {{username}}`

- فهرست کردن همهٔ کاربران:

`marzban cli user list`

- انتقال مالکیت کاربر به مدیر دیگر:

`marzban cli user set-owner {{[-u|--username]}} {{username}} --owner {{owner}}`

- تولید پیکربندی اشتراک برای کاربر:

`marzban cli subscription get-config {{[-u|--username]}} {{username}} {{[-f|--format]}} {{v2ray|clash}}`

- نمایش پیوند اشتراک کاربر:

`marzban cli subscription get-link {{[-u|--username]}} {{username}}`

- نمایش راهنما:

`marzban cli --help`
