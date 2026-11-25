# dos2unix

> تغییر پایان خط به سبک DOS به سبک یونیکس.
> جایگزینی CRLF با LF.
> همچنین ببینید: `unix2dos`, `unix2mac`, `mac2unix`.
> اطلاعات بیشتر: <https://manned.org/dos2unix>.

- تغییر پایان خط‌های یک فایل:

`dos2unix {{path/to/file}}`

- ایجاد نسخه‌ای با پایان خط به سبک یونیکس:

`dos2unix {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- نمایش اطلاعات فایل:

`dos2unix {{[-i|--info]}} {{path/to/file}}`

- نگه داشتن، افزودن یا حذف نشان ترتیب بایت (BOM):

`dos2unix --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
