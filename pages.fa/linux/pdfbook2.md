# pdfbook2

> ساخت کتابچهٔ PDF قابل چاپ دورو از PDF.
> توجه: کتابچه باید به‌صورت دورو در حالت افقی و با برگرداندن از لبهٔ بلند چاپ شود.
> اطلاعات بیشتر: <https://github.com/jenom/pdfbook2#examples>.

- ایجاد کتابچه‌ای به نام `file-book.pdf` با پیش‌فرض‌های مناسب:

`pdfbook2 {{path/to/file.pdf}}`

- ایجاد کتابچه با اندازهٔ کاغذ A4:

`pdfbook2 {{[-p|--paper]}} a4paper {{path/to/file.pdf}}`

- ایجاد کتابچه با حاشیهٔ داخلی کاهش‌یافته به ۵۰ پیکسل (پیش‌فرض = 150px):

`pdfbook2 {{[-p|--paper]}} a4paper {{[-i|--inner-margin]}} 50 {{path/to/file.pdf}}`

- سازمان‌دهی فایل بزرگ با دسته‌های چاپی برای صحافی در کتابچهٔ بزرگ‌تر (تعداد صفحات هر دسته باید بر ۴ بخش‌پذیر باشد):

`pdfbook2 {{[-p|--paper]}} a4paper --signature {{24}} {{path/to/file.pdf}}`
