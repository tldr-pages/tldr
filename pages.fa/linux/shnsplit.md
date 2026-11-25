# shnsplit

> تقسیم فایل‌های صوتی مطابق فایل `.cue`.
> اطلاعات بیشتر: <http://shnutils.freeshell.org/shntool/>.

- تقسیم فایل `.wav` همراه با `.cue` به چند فایل:

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}}`

- نمایش قالب‌های پشتیبانی‌شده:

`shnsplit -a`

- تقسیم فایل `.flac` به چند فایل:

`shnsplit -f {{path/to/file.cue}} -o flac {{path/to/file.flac}}`

- تقسیم فایل `.wav` به فایل‌هایی به‌شکل «شمارهٔ ترک - آلبوم - عنوان»:

`shnsplit -f {{path/to/file.cue}} {{path/to/file.wav}} -t "%n - %a - %t"`
