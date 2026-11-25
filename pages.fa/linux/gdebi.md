# gdebi

> نصب آسان فایل‌های `.deb`.
> اطلاعات بیشتر: <https://manned.org/gdebi>.

- نصب بسته‌های محلی `.deb` همراه با حل و نصب وابستگی‌های آن‌ها:

`gdebi {{path/to/package.deb}}`

- نمایش ندادن اطلاعات پیشرفت:

`gdebi {{path/to/package.deb}} {{[-q|--quiet]}}`

- تنظیم یک گزینهٔ پیکربندی APT:

`gdebi {{path/to/package.deb}} {{[-o|--option]}} {{apt_options}}`

- استفاده از دایرکتوری ریشهٔ جایگزین:

`gdebi {{path/to/package.deb}} --root {{path/to/root_directory}}`

- نمایش نسخه:

`gdebi --version`
