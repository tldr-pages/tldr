# eyeD3

> خواندن و تغییر فرادادهٔ فایل‌های MP3.
> اطلاعات بیشتر: <https://manned.org/eyeD3>.

- مشاهدهٔ اطلاعات یک فایل MP3:

`eyeD3 {{filename.mp3}}`

- تنظیم عنوان یک فایل MP3:

`eyeD3 {{[-t|--title]}} "{{A Title}}" {{filename.mp3}}`

- تنظیم آلبوم همهٔ فایل‌های MP3 در یک دایرکتوری:

`eyeD3 {{[-A|--album]}} "{{Album Name}}" {{*.mp3}}`

- تنظیم تصویر جلد جلویی برای یک فایل MP3:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
