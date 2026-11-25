# imhex

> ویرایشگر شانزده‌شانزدهی برای مهندسان معکوس و برنامه‌نویسان.
> اطلاعات بیشتر: <https://docs.werwolv.net/imhex>.

- باز کردن فایل در ImHex:

`imhex {{path/to/file}}`

- ایجاد فایل خالی جدید:

`imhex --new`

- باز کردن فایل در نمونهٔ در حال اجرای ImHex و انتخاب محدوده‌ای از بایت‌ها (آفست‌ها به‌صورت شانزده‌شانزدهی):

`imhex --open {{path/to/file}} --select {{0xstart_offset}} {{0xend_offset}}`

- نمایش اطلاعات فایل:

`imhex --file-info {{path/to/file}}`

- محاسبهٔ هش فایل با الگوریتم مشخص:

`imhex --hash {{md5|sha1|sha224|sha256|sha384|sha512}} {{path/to/file}}`

- تولید نمایش شانزده‌شانزدهی فایل:

`imhex --hexdump {{path/to/file}}`

- نمایش نسخه:

`imhex --version`
