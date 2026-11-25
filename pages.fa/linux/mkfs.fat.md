# mkfs.fat

> ایجاد فایل‌سیستم MS-DOS داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.fat>.

- ایجاد فایل‌سیستم fat داخل پارتیشن `Y` روی دستگاه `X`:

`sudo mkfs.fat {{/dev/sdXY}}`

- ایجاد فایل‌سیستم با نام حجم:

`sudo mkfs.fat -n {{volume_name}} {{/dev/sdXY}}`

- ایجاد فایل‌سیستم با شناسهٔ حجم:

`sudo mkfs.fat -i {{volume_id}} {{/dev/sdXY}}`

- استفاده از ۴ جدول تخصیص فایل به‌جای ۲ جدول:

`sudo mkfs.fat -f 4 {{/dev/sdXY}}`

- تعیین نوع فایل‌سیستم:

`sudo mkfs.fat -F {{12|16|32}} {{/dev/sdXY}}`
