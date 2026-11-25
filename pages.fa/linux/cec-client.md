# cec-client

> مدیریت اتصال‌های CEC روی گذرگاه سریال.
> همچنین : `cec-ctl`.
> اطلاعات بیشتر: <https://manned.org/cec-client>.

- فهرست کردن همهٔ آداپتورهای CEC:

`cec-client {{[-l|--list-devices]}}`

- شروع یک نشست تعاملی CEC:

`sudo cec-client`

- تنظیم نام نمایش روی صفحه (OSD):

`sudo cec-client {{[-o|--osd-name]}} {{name}}`

- ارسال یک دستور واحد:

`echo {{on 0}} | sudo cec-client {{[-s|--single-command]}}`

- [تعاملی] قرار دادن یک دستگاه در حالت آماده‌به‌کار:

`standby {{0}}`

- [تعاملی] روشن کردن یک دستگاه:

`on {{0}}`
