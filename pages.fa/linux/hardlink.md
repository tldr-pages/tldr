# hardlink

> یکپارچه کردن فایل‌های تکراری با جایگزینی آن‌ها با پیوند سخت.
> بخشی از `util-linux` و مفید برای صرفه‌جویی در فضای دیسک هنگام وجود فایل‌های یکسان در دایرکتوری‌ها است.
> اطلاعات بیشتر: <https://manned.org/hardlink>.

- شبیه‌سازی ایجاد پیوند سخت برای فایل‌های تکراری بدون تغییر آن‌ها:

`hardlink {{[-n|--dry-run]}} {{path/to/directory}}`

- ایجاد پیوند سخت برای فایل‌های تکراری در یک دایرکتوری:

`hardlink {{path/to/directory}}`

- ایجاد پیوند سخت برای فایل‌های تکراری در چند دایرکتوری:

`hardlink {{path/to/directory1 path/to/directory2 ...}}`

- نمایش خروجی مفصل هنگام ایجاد پیوند سخت:

`hardlink {{[-v|--verbose]}} {{path/to/directory}}`

- در نظر گرفتن فقط فایل‌هایی با حداقل اندازهٔ مشخص:

`hardlink {{[-s|--minimum-size]}} {{size}} {{path/to/directory}}`
