# loadkeys

> بارگذاری نگاشت کلید هسته برای کنسول.
> همچنین : `localectl`.
> اطلاعات بیشتر: <https://manned.org/loadkeys>.

- بارگذاری چیدمان صفحه‌کلید مشخص برای کنسول فعلی:

`sudo loadkeys {{en|de|fi|dvorak|defkeymap|...}}`

- بارگذاری نگاشت کلید پیش‌فرض:

`sudo loadkeys {{[-d|--default]}}`

- چاپ جدول منبع هستهٔ یک نگاشت کلید در `stdout`:

`loadkeys {{[-m|--mktable]}} {{en|de|fi|...}}`

- چاپ قالب دودویی نگاشت کلید در `stdout`:

`loadkeys {{[-b|--bkeymap]}} {{en|de|fi|...}}`

- جست‌وجو و تجزیهٔ نگاشت کلید بدون انجام عمل:

`loadkeys {{[-p|--parse]}} {{en|de|fi|...}}`

- بارگذاری نگاشت کلید از `stdin` بدون نمایش خروجی:

`{{command}} | sudo loadkeys {{[-q|--quiet]}}`

- تنظیم نگاشت کلید برای کنسول مشخص:

`sudo loadkeys {{[-C|--console]}} {{/dev/ttyN}} {{uk}}`

- بارگذاری نگاشت کلید از فایل مشخص برای کنسول:

`sudo loadkeys {{[-C|--console]}} {{/dev/ttyN}} /{{path/to/file}}`
