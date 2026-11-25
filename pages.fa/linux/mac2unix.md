# mac2unix

> تغییر پایان خط‌های سبک macOS به سبک Unix.
> کاراکتر CR را با LF جایگزین می‌کند.
> همچنین : `unix2dos`, `unix2mac`, `dos2unix`.
> اطلاعات بیشتر: <https://manned.org/mac2unix>.

- تغییر پایان خط‌های فایل:

`mac2unix {{path/to/file}}`

- ایجاد نسخه‌ای با پایان خط‌های سبک Unix:

`mac2unix {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- نمایش اطلاعات فایل:

`mac2unix {{[-i|--info]}} {{path/to/file}}`

- حفظ، افزودن یا حذف نشان ترتیب بایت:

`mac2unix --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
