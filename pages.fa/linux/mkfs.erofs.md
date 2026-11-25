# mkfs.erofs

> ایجاد فایل‌سیستم EROFS در یک تصویر.
> اطلاعات بیشتر: <https://manned.org/mkfs.erofs>.

- ایجاد فایل‌سیستم EROFS بر اساس دایرکتوری ریشه:

`mkfs.erofs image.erofs root/`

- ایجاد تصویر EROFS با UUID مشخص:

`mkfs.erofs -U {{uuid}} image.erofs root/`

- ایجاد تصویر فشردهٔ EROFS:

`mkfs.erofs -zlz4hc image.erofs root/`

- ایجاد تصویر EROFS که مالک همهٔ فایل‌های آن root است:

`mkfs.erofs --all-root image.erofs root/`
