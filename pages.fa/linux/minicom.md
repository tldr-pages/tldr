# minicom

> ارتباط با واسط سریال دستگاه.
> همچنین : `picocom`, `cu`, `tio`.
> اطلاعات بیشتر: <https://manned.org/minicom>.

- باز کردن پورت سریال مشخص:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}}`

- باز کردن پورت سریال مشخص با نرخ باد مشخص:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-b|--baudrate]}} {{115200}}`

- ورود به منوی پیکربندی پیش از ارتباط با پورت سریال مشخص:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-s|--setup]}}`

- ذخیرهٔ خروجی پورت سریال در فایل:

`sudo minicom {{[-D|--device]}} {{/dev/ttyXYZ}} {{[-C|--capturefile]}} {{path/to/file}}`

- خروج از minicom:

`<Ctrl a><x><Enter>`

- نمایش راهنما:

`minicom {{[-h|--help]}}`
