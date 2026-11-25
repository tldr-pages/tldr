# mkfs.cramfs

> ایجاد فایل‌سیستم ROM داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.cramfs>.

- ایجاد فایل‌سیستم ROM از یک دایرکتوری داخل پارتیشن Y روی دستگاه X:

`sudo mkfs.cramfs {{path/to/directory}} {{/dev/sdXY}}`

- ایجاد فایل‌سیستم ROM با نام حجم:

`sudo mkfs.cramfs -n {{volume_name}} {{path/to/directory}} {{/dev/sdXY}}`
