# pdfcrop

> تشخیص و حذف حاشیه‌های هر صفحه در فایل PDF.
> اطلاعات بیشتر: <https://github.com/ho-tex/pdfcrop>.

- تشخیص و حذف خودکار حاشیهٔ هر صفحه در فایل PDF:

`pdfcrop {{path/to/input_file.pdf}} {{path/to/output_file.pdf}}`

- تنظیم حاشیه‌های هر صفحه به مقدار مشخص:

`pdfcrop {{path/to/input_file.pdf}} --margins '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- تنظیم حاشیه‌های هر صفحه به مقدار مشخص و یکسان برای چپ، بالا، راست و پایین:

`pdfcrop {{path/to/input_file.pdf}} --margins {{300}} {{path/to/output_file.pdf}}`

- استفاده از کادر محدودکنندهٔ تعریف‌شده توسط کاربر برای برش به‌جای تشخیص خودکار:

`pdfcrop {{path/to/input_file.pdf}} --bbox '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- استفاده از کادرهای محدودکنندهٔ متفاوت تعریف‌شده توسط کاربر برای صفحات فرد و زوج:

`pdfcrop {{path/to/input_file.pdf}} --bbox-odd '{{left}} {{top}} {{right}} {{bottom}}' --bbox-even '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- تشخیص خودکار حاشیه‌ها با وضوح کمتر برای بهبود عملکرد:

`pdfcrop {{path/to/input_file.pdf}} --resolution {{72}} {{path/to/output_file.pdf}}`
