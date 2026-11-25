# pstoedit

> تبدیل فایل‌های PDF به قالب‌های مختلف تصویر.
> اطلاعات بیشتر: <http://www.calvina.de/pstoedit/pstoedit.htm>.

- تبدیل صفحهٔ PDF به قالب PNG یا JPEG:

`pstoedit -page {{page_number}} -f magick {{path/to/file.pdf}} {{page}}.{{png|jpg}}`

- تبدیل چند صفحهٔ PDF به تصاویر شماره‌گذاری‌شده:

`pstoedit -f magick {{path/to/file}} {{page%d}}.{{png|jpg}}`
