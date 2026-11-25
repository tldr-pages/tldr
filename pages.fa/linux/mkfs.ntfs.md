# mkfs.ntfs

> ایجاد فایل‌سیستم NTFS داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.ntfs>.

- ایجاد فایل‌سیستم NTFS داخل پارتیشن Y روی دستگاه X:

`sudo mkfs.ntfs {{/dev/sdXY}}`

- ایجاد فایل‌سیستم با برچسب حجم:

`sudo mkfs.ntfs {{[-L|--label]}} {{volume_label}} {{/dev/sdXY}}`

- ایجاد فایل‌سیستم با UUID مشخص:

`sudo mkfs.ntfs {{[-U|--with-uuid]}} {{uuid}} {{/dev/sdXY}}`
