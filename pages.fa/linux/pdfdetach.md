# pdfdetach

> فهرست یا استخراج پیوست‌ها (فایل‌های جاسازی‌شده) از فایل PDF.
> همچنین : `pdfattach`, `pdfimages`, `pdfinfo`.
> اطلاعات بیشتر: <https://manned.org/pdfdetach>.

- فهرست کردن همهٔ پیوست‌های فایل با رمزگذاری متن مشخص:

`pdfdetach list -enc {{UTF-8}} {{path/to/input.pdf}}`

- ذخیرهٔ فایل جاسازی‌شدهٔ مشخص با تعیین شمارهٔ آن:

`pdfdetach -save {{number}} {{path/to/input.pdf}}`

- ذخیرهٔ فایل جاسازی‌شدهٔ مشخص با تعیین نام آن:

`pdfdetach -savefile {{name}} {{path/to/input.pdf}}`

- ذخیرهٔ فایل جاسازی‌شده با نام خروجی دلخواه:

`pdfdetach -save {{number}} -o {{path/to/output}} {{path/to/input.pdf}}`

- ذخیرهٔ پیوست از فایل محافظت‌شده با رمز عبور مالک یا کاربر:

`pdfdetach -save {{number}} {{-opw|-upw}} {{password}} {{path/to/input.pdf}}`
