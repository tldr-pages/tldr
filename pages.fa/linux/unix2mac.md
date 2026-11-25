# unix2mac

> تغییر پایان خط‌های سبک Unix به سبک macOS.
> کاراکتر LF را با CR جایگزین می‌کند.
> همچنین ببینید: `unix2dos`, `dos2unix`, `mac2unix`.
> اطلاعات بیشتر: <https://manned.org/unix2mac>.

- تغییر پایان خط‌های فایل:

`unix2mac {{path/to/file}}`

- ایجاد نسخه‌ای با پایان خط‌های سبک macOS:

`unix2mac {{[-n|--newfile]}} {{path/to/file}} {{path/to/new_file}}`

- نمایش اطلاعات فایل:

`unix2mac {{[-i|--info]}} {{path/to/file}}`

- حفظ، افزودن یا حذف نشان ترتیب بایت:

`unix2mac --{{keep-bom|add-bom|remove-bom}} {{path/to/file}}`
