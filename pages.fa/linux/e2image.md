# e2image

> ذخیرهٔ فرادادهٔ حیاتی سیستم فایل ext2/ext3/ext4 در یک فایل.
> اطلاعات بیشتر: <https://manned.org/e2image>.

- نوشتن فرادادهٔ موجود روی دستگاه در فایل مشخص:

`e2image {{/dev/sdXN}} {{path/to/image_file}}`

- چاپ فرادادهٔ موجود روی دستگاه در خروجی استاندارد `stdout`:

`e2image {{/dev/sdXN}} -`

- بازگرداندن فرادادهٔ سیستم فایل به دستگاه:

`e2image -I {{/dev/sdXN}} {{path/to/image_file}}`

- ایجاد فایل خام و تنک بزرگ با `-r` و فراداده در آفست‌های مناسب:

`e2image -r {{/dev/sdXN}} {{path/to/image_file}}`

- ایجاد فایل تصویر QCOW2 با `-Q` به جای تصویر عادی یا خام:

`e2image -Q {{/dev/sdXN}} {{path/to/image_file}}`
