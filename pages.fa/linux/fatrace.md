# fatrace

> گزارش رویدادهای دسترسی به فایل.
> همچنین ببینید: `inotifywait`.
> اطلاعات بیشتر: <https://manned.org/fatrace>.

- چاپ رویدادهای دسترسی به فایل در همهٔ سیستم‌های فایل سوارشده در خروجی استاندارد `stdout`:

`sudo fatrace`

- محدود کردن خروجی به برنامه‌ای با نام مشخص:

`sudo fatrace {{[-C|--command]}} {{program_name}}`

- چاپ رویدادهای دسترسی به فایل در سیستم فایل سوارشدهٔ دایرکتوری فعلی در `stdout`:

`sudo fatrace {{[-c|--current-mount]}}`

- افزودن زمان به خروجی:

`sudo fatrace {{[-t|--timestamp]}}`
