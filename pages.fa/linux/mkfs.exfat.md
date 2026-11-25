# mkfs.exfat

> ایجاد فایل‌سیستم exfat داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.exfat>.

- ایجاد فایل‌سیستم exfat داخل پارتیشن Y روی دستگاه X:

`sudo mkfs.exfat {{/dev/sdXY}}`

- ایجاد فایل‌سیستم با نام حجم:

`sudo mkfs.exfat {{[-L|--volume-label]}} {{volume_name}} {{/dev/sdXY}}`

- ایجاد فایل‌سیستم با شناسهٔ حجم:

`sudo mkfs.exfat {{[-U|--volume-guid]}} {{volume_id}} {{/dev/sdXY}}`
