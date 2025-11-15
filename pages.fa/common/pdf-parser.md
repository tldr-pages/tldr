# pdf-parser

> عناصر اساسی یک فایل پی دی اف را بدون رندر کردن آن مشخص می کند.
> اطلاعات بیشتر: <https://blog.didierstevens.com/programs/pdf-tools>.

- نمایش آمار مربوط به یک فایل پی دی اف:

`pdf-parser {{[-a|--stats]}} {{path/to/file.pdf}}`

- نمایش اشیاء از یک نوع خاص (`/Font`, `/URI`, ...) در یک فایل پی دی اف:

`pdf-parser {{[-t|--type]}} {{/object_type}} {{path/to/file.pdf}}`

- جستجوی رشته ها در اشیاء غیرمستقیم:

`pdf-parser {{[-s|--search]}} {{search_string}} {{path/to/file.pdf}}`
