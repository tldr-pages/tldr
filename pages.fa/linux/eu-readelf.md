# eu-readelf

> نمایش اطلاعات فایل‌های ELF.
> اطلاعات بیشتر: <https://manned.org/eu-readelf>.

- نمایش همهٔ اطلاعات قابل استخراج موجود در فایل ELF:

`eu-readelf {{[-a|--all]}} {{path/to/file}}`

- نمایش محتوای همهٔ قطعه‌ها یا بخش‌های NOTE، یا یک قطعه یا بخش مشخص:

`eu-readelf {{[-n|--notes]}} {{.note.ABI-tag}} {{path/to/file}}`
