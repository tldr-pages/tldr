# rc-update

> افزودن و حذف سرویس‌های OpenRC به سطوح اجرا یا از آن‌ها.
> همچنین ببینید: `openrc`.
> اطلاعات بیشتر: <https://manned.org/rc-update>.

- فهرست کردن سرویس‌های فعال و سطوح اجرای مربوط:

`rc-update`

- فهرست کردن همهٔ سرویس‌ها:

`rc-update {{[-v|--verbose]}}`

- افزودن سرویس به سطح اجرا:

`sudo rc-update add {{service_name}} {{runlevel}}`

- حذف سرویس از سطح اجرا:

`sudo rc-update {{[del|delete]}} {{service_name}} {{runlevel}}`

- حذف سرویس از همهٔ سطوح اجرا:

`sudo rc-update {{[-a|--all]}} {{[del|delete]}} {{service_name}}`
