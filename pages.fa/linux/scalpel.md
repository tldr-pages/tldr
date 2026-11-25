# scalpel

> بازیابی فایل‌ها از تصویر دیسک بر اساس سربرگ و پانوشت فایل.
> الگوهای فایل باید در فایل پیکربندی فعال شوند (به‌طور پیش‌فرض همه در حالت توضیح هستند).
> اطلاعات بیشتر: <https://manned.org/scalpel>.

- استخراج فایل‌ها از تصویر دیسک با فایل پیکربندی مشخص:

`scalpel -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- پیش‌نمایش فایل‌های قابل استخراج بدون استخراج واقعی:

`scalpel -p -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- رد کردن N بایت نخست تصویر دیسک پیش از استخراج:

`scalpel -s {{number}} -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- استخراج فایل‌ها بدون سازمان‌دهی در زیردایرکتوری‌ها بر اساس نوع:

`scalpel -O -c {{path/to/scalpel.conf}} -o {{path/to/output_directory}} {{path/to/disk_image.dd}}`

- نمایش راهنما:

`scalpel -h`

- نمایش نسخه:

`scalpel -V`
