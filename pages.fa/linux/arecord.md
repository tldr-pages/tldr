# arecord

> ضبط‌کنندهٔ صدا برای درایور کارت صدای ALSA.
> اطلاعات بیشتر: <https://manned.org/arecord>.

- ضبط یک قطعه صدا با کیفیت «CD» (پس از اتمام با `<Ctrl c>` پایان دهید):

`arecord {{[-vv|--verbose --verbose]}} {{[-f|--format]}} cd {{path/to/file.wav}}`

- ضبط یک قطعه صدا با کیفیت «CD» و مدت ثابت ۱۰ ثانیه:

`arecord {{[-vv|--verbose --verbose]}} {{[-f|--format]}} cd {{[-d|--duration]}} 10 {{path/to/file.wav}}`

- ضبط یک قطعه صدا و ذخیرهٔ آن به‌صورت MP3 (پس از اتمام با `<Ctrl c>` پایان دهید):

`arecord {{[-vv|--verbose --verbose]}} {{[-f|--format]}} cd {{[-t|--file-type]}} raw | lame -r - {{path/to/file.mp3}}`

- فهرست کردن همهٔ کارت‌های صدا و دستگاه‌های صوتی دیجیتال:

`arecord {{[-l|--list-devices]}}`

- فعال کردن رابط تعاملی (برای مثال استفاده از `<Space>` یا `<Enter>` برای پخش یا مکث):

`arecord {{[-i|--interactive]}}`

- آزمودن میکروفون با ضبط و پخش یک نمونهٔ ۵ ثانیه‌ای:

`arecord {{[-d|--duration]}} 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav`
