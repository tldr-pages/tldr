# abrt-action-analyze-backtrace

> تحلیل رد فراخوانی C/C++.
> تولید هش تشخیص موارد تکراری، ارزیابی رد فراخوانی و شناسایی تابع محل خرابی.
> ذخیرهٔ داده‌ها به‌صورت عناصر جدید `duphash`، `rating` و `crash_function` در دایرکتوری مشکل.
> اطلاعات بیشتر: <https://manned.org/abrt-action-analyze-backtrace>.

- تحلیل رد فراخوانی برای دایرکتوری کاری فعلی:

`abrt-action-analyze-backtrace`

- تحلیل رد فراخوانی برای یک دایرکتوری مشخص:

`abrt-action-analyze-backtrace -d {{path/to/directory}}`

- تحلیل رد فراخوانی با خروجی مفصل:

`abrt-action-analyze-backtrace -v`
