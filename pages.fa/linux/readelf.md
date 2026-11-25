# readelf

> نمایش اطلاعات فایل‌های ELF.
> اطلاعات بیشتر: <https://manned.org/readelf>.

- نمایش همهٔ اطلاعات فایل ELF:

`readelf {{[-a|--all]}} {{path/to/binary}}`

- نمایش همهٔ سربرگ‌های موجود در فایل ELF:

`readelf {{[-e|--headers]}} {{path/to/binary}}`

- نمایش مدخل‌های بخش جدول نماد فایل ELF، در صورت وجود:

`readelf {{[-s|--symbols]}} {{path/to/binary}}`

- نمایش اطلاعات سربرگ ELF:

`readelf {{[-h|--file-header]}} {{path/to/binary}}`

- نمایش اطلاعات سربرگ بخش‌های ELF:

`readelf {{[-S|--section-headers]}} {{path/to/binary}}`

- نمایش اطلاعات DWARF:

`readelf {{[-w|--debug-dump]}} {{path/to/binary}}`
