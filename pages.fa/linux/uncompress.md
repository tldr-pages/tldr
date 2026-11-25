# uncompress

> خارج کردن فایل‌های فشرده‌شده با دستور Unix به نام `compress` از حالت فشرده.
> اطلاعات بیشتر: <https://manned.org/uncompress>.

- خارج کردن فایل‌های مشخص از حالت فشرده:

`uncompress {{path/to/file1.Z path/to/file2.Z ...}}`

- خارج کردن فایل‌های مشخص از حالت فشرده با نادیده گرفتن موارد ناموجود:

`uncompress -f {{path/to/file1.Z path/to/file2.Z ...}}`

- نوشتن در `stdout` (هیچ فایلی تغییر نمی‌کند و هیچ فایل `.Z` ایجاد نمی‌شود):

`uncompress -c {{path/to/file1.Z path/to/file2.Z ...}}`

- خارج کردن فایل‌ها از حالت فشرده با خروجی مفصل (نوشتن درصد کاهش یا افزایش در `stderr`):

`uncompress -v {{path/to/file1.Z path/to/file2.Z ...}}`
