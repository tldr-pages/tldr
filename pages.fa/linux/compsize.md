# compsize

> محاسبهٔ نسبت فشرده‌سازی مجموعه‌ای از فایل‌ها در سیستم فایل btrfs.
> همچنین : `btrfs filesystem`.
> اطلاعات بیشتر: <https://manned.org/compsize>.

- محاسبهٔ نسبت فشرده‌سازی فعلی یک فایل یا دایرکتوری:

`sudo compsize {{path/to/file_or_directory}}`

- عبور نکردن از مرز سیستم‌های فایل:

`sudo compsize {{[-x|--one-file-system]}} {{path/to/file_or_directory}}`

- نمایش تعداد خام بایت‌ها به جای اندازه‌های خوانا:

`sudo compsize {{[-b|--bytes]}} {{path/to/file_or_directory}}`
