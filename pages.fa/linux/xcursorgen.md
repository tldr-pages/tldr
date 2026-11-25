# xcursorgen

> ایجاد فایل اشاره‌گر X از مجموعه‌ای از فایل‌های PNG.
> اگر `--prefix` حذف شود، فایل‌های تصویر باید در دایرکتوری کاری فعلی باشند.
> اطلاعات بیشتر: <https://manned.org/xcursorgen>.

- ایجاد فایل اشاره‌گر X با فایل پیکربندی:

`xcursorgen {{path/to/config.cursor}} {{path/to/output_file}}`

- ایجاد فایل اشاره‌گر X با فایل پیکربندی و تعیین مسیر فایل‌های تصویر:

`xcursorgen --prefix {{path/to/image_directory}}/ {{path/to/config.cursor}} {{path/to/output_file}}`

- ایجاد فایل اشاره‌گر X با فایل پیکربندی و نوشتن خروجی در `stdout`:

`xcursorgen {{path/to/config.cursor}}`
