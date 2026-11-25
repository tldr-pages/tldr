# mkisofs

> ایجاد فایل‌های ISO از دایرکتوری‌ها.
> همچنین نام مستعار آن `genisoimage` است.
> اطلاعات بیشتر: <https://manned.org/mkisofs>.

- ایجاد ISO از دایرکتوری:

`mkisofs -o {{filename.iso}} {{path/to/source_directory}}`

- تنظیم برچسب دیسک هنگام ایجاد ISO:

`mkisofs -o {{filename.iso}} -V "{{label_name}}" {{path/to/source_directory}}`

- ایجاد تصویر ISO با فایل‌های بزرگ‌تر از 2GiB با گزارش اندازهٔ ظاهری کوچک‌تر برای فایل‌سیستم‌های ISO9660:

`mkisofs -o {{filename.iso}} -allow-limited-size {{path/to/source_directory}}`
