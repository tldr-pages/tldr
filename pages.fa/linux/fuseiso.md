# fuseiso

> ماژول FUSE برای سوار کردن تصاویر سیستم فایل ISO، BIN، NRG، MDF و IMG.
> اطلاعات بیشتر: <https://manned.org/fuseiso>.

- سوار کردن تصویر ISO در دایرکتوری مشخص:

`fuseiso {{path/to/image.iso}} {{path/to/mount_point}}`

- سوار کردن تصویر ISO با ایجاد خودکار نقطهٔ اتصال در صورت نبودن و حذف آن هنگام پیاده کردن:

`fuseiso -p {{path/to/image.iso}} {{path/to/mount_point}}`

- سوار کردن تصویر ISO در پیش‌زمینه (مفید برای اشکال‌زدایی):

`fuseiso -f {{path/to/image.iso}} {{path/to/mount_point}}`

- پیاده کردن تصویر با ابزار استاندارد پیاده‌سازی FUSE:

`fusermount -u {{path/to/mount_point}}`
