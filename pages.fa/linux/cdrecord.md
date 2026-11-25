# cdrecord

> ضبط داده روی CD یا DVD.
> برخی نحوه‌های اجرای cdrecord ممکن است باعث عملیات مخرب مانند پاک کردن همهٔ داده‌های یک دیسک شوند.
> اطلاعات بیشتر: <https://manned.org/cdrecord>.

- نمایش درایوهای نوری در دسترس `cdrecord`:

`cdrecord --devices`

- رایت یک دیسک فقط صوتی:

`cdrecord dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- رایت یک فایل روی دیسک و بیرون دادن دیسک پس از پایان (برخی دستگاه‌های رایت به این کار نیاز دارند):

`cdrecord -eject dev={{/dev/optical_drive}} -data {{file.iso}}`

- رایت یک فایل روی دیسک در درایو نوری، با امکان نوشتن روی چند دیسک به‌صورت متوالی:

`cdrecord -tao dev={{/dev/optical_drive}} -data {{file.iso}}`
