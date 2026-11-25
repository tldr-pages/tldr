# pdftohtml

> تبدیل فایل‌های PDF به HTML، XML و تصاویر PNG.
> اطلاعات بیشتر: <https://manned.org/pdftohtml>.

- تبدیل فایل PDF به فایل HTML:

`pdftohtml {{path/to/file.pdf}} {{path/to/output_file.html}}`

- نادیده گرفتن تصاویر فایل PDF:

`pdftohtml -i {{path/to/file.pdf}} {{path/to/output_file.html}}`

- تولید یک فایل HTML شامل همهٔ صفحات PDF:

`pdftohtml -s {{path/to/file.pdf}} {{path/to/output_file.html}}`

- تبدیل فایل PDF به فایل XML:

`pdftohtml -xml {{path/to/file.pdf}} {{path/to/output_file.xml}}`
