# bchunk

> تبدیل تصاویر CD به مجموعه‌ای از ترک‌های `.iso` و `.cdr`.
> اطلاعات بیشتر: <https://manned.org/bchunk>.

- تبدیل تصویر دودویی CD به یک فایل تصویر استاندارد iso9960:

`bchunk {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- تبدیل با خروجی مفصل:

`bchunk -v {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- تولید فایل‌های صوتی در قالب WAV:

`bchunk -w {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`
