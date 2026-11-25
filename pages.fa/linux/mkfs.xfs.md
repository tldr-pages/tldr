# mkfs.xfs

> ایجاد فایل‌سیستم XFS داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.xfs>.

- ایجاد فایل‌سیستم XFS داخل پارتیشن Y روی دستگاه X:

`sudo mkfs.xfs {{/dev/sdXY}}`

- ایجاد فایل‌سیستم XFS با برچسب حجم:

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdXY}}`
