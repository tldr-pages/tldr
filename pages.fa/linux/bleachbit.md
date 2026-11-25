# bleachbit

> پاکسازی فایل‌های زائد در سیستم فایل.
> اطلاعات بیشتر: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- شروع نسخهٔ رابط گرافیکی Bleachbit:

`bleachbit --gui`

- حذف امن یک فایل با بازنویسی آن:

`bleachbit {{[-s|--shred]}} {{path/to/file}}`

- فهرست کردن گزینه‌های پاک‌کنندهٔ موجود:

`bleachbit {{[-l|--list-cleaners]}}`

- پیش‌نمایش فایل‌هایی که حذف خواهند شد و دیگر تغییرات، پیش از اجرای واقعی عملیات پاکسازی:

`bleachbit {{[-p|--preview]}} --preset {{cleaner1.option1 cleaner2.option2 ...}}`

- اجرای عملیات پاکسازی و حذف فایل‌ها:

`bleachbit {{[-c|--clean]}} --preset {{cleaner1.option1 cleaner2.option2 ...}}`
