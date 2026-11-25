# gs

> GhostScript، مفسر PDF و PostScript.
> اطلاعات بیشتر: <https://manned.org/gs>.

- مشاهدهٔ یک فایل:

`gs -dQUIET -dBATCH {{file.pdf}}`

- کاهش اندازهٔ فایل PDF به تصاویر با وضوح ۱۵۰ dpi برای خواندن در دستگاه کتاب‌خوان:

`gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile={{output.pdf}} {{input.pdf}}`

- تبدیل صفحه‌های ۱ تا ۳ فایل PDF به تصویر با وضوح ۱۵۰ dpi:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dFirstPage=1 -dLastPage=3 -sOutputFile={{output_%d.jpg}} {{input.pdf}}`

- استخراج صفحه‌ها از فایل PDF:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.pdf}}`

- ادغام فایل‌های PDF:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- تبدیل فایل PostScript به فایل PDF:

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.ps}}`
