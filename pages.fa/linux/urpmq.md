# urpmq

> پرس‌وجوی اطلاعات بسته‌ها و رسانه‌ها در Mageia.
> همچنین : `urpmi`, `urpmi.update`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpme`.
> اطلاعات بیشتر: <https://man.linuxreviews.org/man8/urpmq.8.html>.

- نمایش اطلاعات بستهٔ قابل نصب:

`urpmq -i {{package}}`

- نمایش وابستگی‌های مستقیم بسته:

`urpmq --requires {{package}}`

- نمایش وابستگی‌های مستقیم و غیرمستقیم بسته:

`urpmq {{[-d|--requires-recursive]}} {{package}}`

- فهرست کردن بسته‌های نصب‌نشدهٔ مورد نیاز فایل RPM همراه با منابع آن‌ها:

`sudo urpmq {{[-d|--requires-recursive]}} -m --sources {{path/to/file.rpm}}`

- فهرست کردن همهٔ رسانه‌های پیکربندی‌شده با URL، از جمله رسانه‌های غیرفعال:

`urpmq --list-media --list-url`

- جست‌وجوی بسته و چاپ گروه، نسخه و انتشار:

`urpmq -g -r {{[-y|--fuzzy]}} {{keyword}}`

- جست‌وجوی بسته با نام دقیق:

`urpmq -g -r {{package}}`
