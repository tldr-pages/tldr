# compress

> فشرده‌سازی فایل‌ها با دستور یونیکسی `compress`.
> اطلاعات بیشتر: <https://manned.org/compress>.

- فشرده‌سازی فایل‌های مشخص:

`compress {{path/to/file1 path/to/file2 ...}}`

- فشرده‌سازی فایل‌های مشخص و نادیده گرفتن فایل‌هایی که وجود ندارند:

`compress -f {{path/to/file1 path/to/file2 ...}}`

- تعیین حداکثر تعداد بیت فشرده‌سازی (۹ تا ۱۶ بیت):

`compress -b {{9..16}}`

- نوشتن در خروجی استاندارد `stdout` (هیچ فایلی تغییر نمی‌کند):

`compress -c {{path/to/file}}`

- باز کردن فشرده‌سازی فایل‌ها (مانند `uncompress`):

`compress -d {{path/to/file}}`

- نمایش درصد فشرده‌سازی:

`compress -v {{path/to/file}}`
