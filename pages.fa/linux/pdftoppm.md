# pdftoppm

> تبدیل صفحات سند PDF به Pixmap قابل حمل (قالب‌های تصویر).
> اطلاعات بیشتر: <https://manned.org/pdftoppm>.

- تعیین بازهٔ صفحات برای تبدیل (`n` صفحهٔ نخست، `m` صفحهٔ آخر):

`pdftoppm -f {{n}} -l {{m}} {{path/to/file.pdf}} {{image_name_prefix}}`

- تبدیل فقط صفحهٔ نخست PDF:

`pdftoppm -singlefile {{path/to/file.pdf}} {{image_name_prefix}}`

- تولید فایل PBM تک‌رنگ (به‌جای فایل PPM رنگی):

`pdftoppm -mono {{path/to/file.pdf}} {{image_name_prefix}}`

- تولید فایل PGM خاکستری (به‌جای فایل PPM رنگی):

`pdftoppm -gray {{path/to/file.pdf}} {{image_name_prefix}}`

- تولید فایل PNG به‌جای فایل PPM:

`pdftoppm -png {{path/to/file.pdf}} {{image_name_prefix}}`
