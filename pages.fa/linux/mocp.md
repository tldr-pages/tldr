# mocp

> پخش‌کنندهٔ صوتی Music on Console (MOC).
> اطلاعات بیشتر: <https://manned.org/mocp>.

- اجرای رابط متنی MOC:

`mocp`

- اجرای رابط متنی MOC در دایرکتوری مشخص:

`mocp {{path/to/directory}}`

- شروع سرور MOC در پس‌زمینه بدون اجرای رابط متنی آن:

`mocp {{[-S|--server]}}`

- افزودن آهنگ مشخص به صف پخش در حالی که MOC در پس‌زمینه است:

`mocp {{[-q|--enqueue]}} {{path/to/audio_file}}`

- افزودن بازگشتی آهنگ‌ها به صف پخش در حالی که MOC در پس‌زمینه است:

`mocp {{[-a|--append]}} {{path/to/directory}}`

- پاک کردن صف پخش در حالی که MOC در پس‌زمینه است:

`mocp {{[-c|--clear]}}`

- پخش یا توقف آهنگ فعلی صف در حالی که MOC در پس‌زمینه است:

`mocp --{{play|stop}}`

- توقف سرور MOC در حالی که در پس‌زمینه است:

`mocp {{[-x|--exit]}}`
