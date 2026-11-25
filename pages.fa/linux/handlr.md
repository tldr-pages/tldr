# handlr

> مدیریت برنامه‌های پیش‌فرض.
> اطلاعات بیشتر: <https://github.com/chmln/handlr#usage>.

- باز کردن URL در برنامهٔ پیش‌فرض:

`handlr open {{https://example.com}}`

- باز کردن PDF در نمایشگر پیش‌فرض PDF:

`handlr open {{path/to/file.pdf}}`

- تنظیم `imv` به‌عنوان برنامهٔ پیش‌فرض فایل‌های PNG:

`handlr set {{.png}} {{imv.desktop}}`

- تنظیم MPV به‌عنوان برنامهٔ پیش‌فرض همهٔ فایل‌های صوتی:

`handlr set '{{audio/*}}' {{mpv.desktop}}`

- فهرست کردن همهٔ برنامه‌های پیش‌فرض:

`handlr list`

- چاپ برنامهٔ پیش‌فرض فایل‌های PNG:

`handlr get {{.png}}`
