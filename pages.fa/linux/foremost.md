# foremost

> بازیابی فایل‌ها با استفاده از سربرگ‌ها، پانوشت‌ها و ساختار دادهٔ آن‌ها.
> اطلاعات بیشتر: <https://manned.org/foremost>.

- بازیابی فایل‌های نوع مشخص با `-t` (مانند JPEG) از یک تصویر دیسک:

`foremost -t {{jpg}} -i {{path/to/disk_image.dd}}`

- بازیابی فایل‌های چند نوع با `-t`:

`foremost -t {{gif,png,pdf}} -i {{path/to/disk_image.dd}}`

- بازیابی فایل‌ها با استفاده از همهٔ قالب‌های ازپیش‌تعریف‌شده:

`foremost -t all -i {{path/to/disk_image.dd}}`

- بازیابی فایل‌ها در دایرکتوری خروجی مشخص با `-o`:

`foremost -o {{path/to/output_directory}} -i {{path/to/disk_image.dd}}`

- نمایش راهنما با `-h`:

`foremost -h`

- نمایش نسخه با `-V`:

`foremost -V`
