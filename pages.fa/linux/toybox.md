# toybox

> ابزار چندمنظوره که بسیاری از ابزارهای استاندارد Unix را فراهم می‌کند.
> معمولاً در Android و سیستم‌های لینوکس تعبیه‌شده استفاده می‌شود.
> همچنین ببینید: `busybox`, `coreutils`.
> اطلاعات بیشتر: <https://landley.net/toybox/>.

- فهرست کردن همهٔ دستورهای موجود Toybox:

`toybox`

- اجرای صریح دستور Toybox (اگر دستور هم‌نام دیگری در `$PATH` وجود داشته باشد مفید است):

`toybox {{command}} {{arguments}}`

- فهرست کردن فایل‌های دایرکتوری فعلی:

`toybox ls`

- حذف فایل:

`toybox rm {{path/to/file}}`

- نمایش اطلاعات راهنمای دستور مشخص:

`toybox {{command}} --help`

- نمایش نسخه:

`toybox --version`
