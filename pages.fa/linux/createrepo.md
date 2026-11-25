# createrepo

> مقداردهی اولیهٔ مخزن RPM در یک دایرکتوری، شامل همهٔ فایل‌های XML و SQLite.
> اطلاعات بیشتر: <https://manned.org/createrepo>.

- مقداردهی اولیهٔ یک مخزن پایه در دایرکتوری:

`createrepo {{path/to/directory}}`

- مقداردهی اولیهٔ مخزن، کنار گذاشتن RPMهای آزمایشی و نمایش گزارش مفصل:

`createrepo {{[-v|--verbose]}} {{[-x|--excludes]}} {{test_*.rpm}} {{path/to/directory}}`

- مقداردهی اولیهٔ مخزن با SHA1 به‌عنوان الگوریتم مجموع مقابله‌ای و نادیده گرفتن پیوندهای نمادین:

`createrepo {{[-S|--skip-symlinks]}} {{[-s|--checksum]}} {{sha1}} {{path/to/directory}}`
