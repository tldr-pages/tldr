# unix2dos

> تغییر پایان خط‌های سبک Unix به سبک DOS.
> کاراکتر LF را با CRLF جایگزین می‌کند.
> همچنین ببینید: `unix2mac`, `dos2unix`, `mac2unix`.
> اطلاعات بیشتر: <https://manned.org/unix2dos>.

- تغییر پایان خط‌های فایل:

`unix2dos {{path/to/file}}`

- ایجاد نسخه‌ای با پایان خط‌های سبک DOS:

`unix2dos {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- نمایش اطلاعات فایل:

`unix2dos {{[-i|--info]}} {{path/to/file}}`

- حفظ، افزودن یا حذف نشان ترتیب بایت:

`unix2dos --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
