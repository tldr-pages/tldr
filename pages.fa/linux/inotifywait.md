# inotifywait

> انتظار برای تغییرات فایل‌ها.
> همچنین ببینید: `fatrace`.
> اطلاعات بیشتر: <https://manned.org/inotifywait>.

- پایش یک فایل مشخص برای رویدادها و خروج پس از نخستین رویداد:

`inotifywait {{path/to/file}}`

- پایش پیوستهٔ فایل مشخص برای رویدادها بدون خروج:

`inotifywait {{[-m|--monitor]}} {{path/to/file}}`

- پایش بازگشتی دایرکتوری برای رویدادها:

`inotifywait {{[-m|--monitor]}} {{[-r|--recursive]}} {{path/to/directory}}`

- پایش دایرکتوری برای تغییرات، به‌جز فایل‌هایی که نامشان با `regex` مطابقت دارد:

`inotifywait {{[-m|--monitor]}} {{[-r|--recursive]}} --exclude "{{regex}}" {{path/to/directory}}`

- پایش فایل برای تغییرات و خروج در صورت نبود رویداد به مدت ۳۰ ثانیه:

`inotifywait {{[-m|--monitor]}} {{[-t|--timeout]}} 30 {{path/to/file}}`

- پایش فایل فقط برای رویدادهای تغییر فایل:

`inotifywait {{[-e|--event]}} modify {{path/to/file}}`

- پایش فایل و چاپ فقط رویدادها بدون پیام‌های وضعیت:

`inotifywait {{[-q|--quiet]}} {{path/to/file}}`

- اجرای دستور هنگام دسترسی به فایل:

`inotifywait {{[-e|--event]}} access {{path/to/file}} && {{command}}`
