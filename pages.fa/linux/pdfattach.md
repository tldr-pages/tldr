# pdfattach

> افزودن پیوست جدید (فایل جاسازی‌شده) به فایل PDF موجود.
> همچنین ببینید: `pdfdetach`, `pdfimages`, `pdfinfo`.
> اطلاعات بیشتر: <https://manned.org/pdfattach>.

- افزودن پیوست جدید به فایل PDF موجود:

`pdfattach {{path/to/input.pdf}} {{path/to/file_to_attach}} {{path/to/output.pdf}}`

- جایگزینی پیوست هم‌نام در صورت وجود:

`pdfattach -replace {{path/to/input.pdf}} {{path/to/file_to_attach}} {{path/to/output.pdf}}`

- نمایش راهنما:

`pdfattach {{[-h|--help]}}`

- نمایش نسخه:

`pdfattach -v`
