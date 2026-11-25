# elfedit

> به‌روزرسانی سربرگ ELF و ویژگی‌های برنامه در فایل‌های ELF.
> همچنین ببینید: `readelf`, `objcopy`.
> اطلاعات بیشتر: <https://manned.org/elfedit>.

- تغییر نوع ماشین یک فایل ELF:

`elfedit --output-mach {{x86-64|i386|iamcu|...}} {{path/to/file}}`

- تغییر نوع ماشین فقط در فایل‌هایی که در حال حاضر نوع ماشین مشخصی دارند:

`elfedit --input-mach {{i386}} --output-mach {{iamcu}} {{path/to/file1 path/to/file2 ...}}`

- تغییر نوع فایل به قابل جابه‌جایی، اجرایی یا شیء اشتراکی:

`elfedit --output-type {{rel|exec|dyn}} {{path/to/file}}`

- تغییر OSABI:

`elfedit --output-osabi {{none|Linux|FreeBSD|...}} {{path/to/file}}`

- تغییر نسخهٔ ABI:

`elfedit --output-abiversion {{0..255}} {{path/to/file}}`

- فعال کردن یک قابلیت x86 در فایل اجرایی یا کتابخانهٔ اشتراکی:

`elfedit --enable-x86-feature {{ibt|shstk|lam_u48|lam_u57}} {{path/to/file}}`

- غیرفعال کردن یک قابلیت x86 در فایل اجرایی یا کتابخانهٔ اشتراکی:

`elfedit --disable-x86-feature {{ibt|shstk|lam_u48|lam_u57}} {{path/to/file}}`

- نمایش راهنما:

`elfedit {{[-h|--help]}}`
