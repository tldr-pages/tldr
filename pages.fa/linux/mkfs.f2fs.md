# mkfs.f2fs

> ایجاد فایل‌سیستم F2FS داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.f2fs>.

- ایجاد فایل‌سیستم F2FS داخل پارتیشن Y روی دستگاه X:

`sudo mkfs.f2fs {{/dev/sdXY}}`

- ایجاد فایل‌سیستم F2FS با برچسب حجم:

`sudo mkfs.f2fs -l {{volume_label}} {{/dev/sdXY}}`
