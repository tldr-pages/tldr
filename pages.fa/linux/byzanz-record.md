# byzanz-record

> ضبط صفحه‌نمایش.
> اطلاعات بیشتر: <https://manned.org/byzanz-record>.

- ضبط صفحه و نوشتن نتیجه در یک فایل (به‌صورت پیش‌فرض `byzanz-record` فقط ۱۰ ثانیه ضبط می‌کند):

`byzanz-record {{path/to/file.ext}}`

- نمایش اطلاعات حین ضبط و پس از آن:

`byzanz-record {{[-v|--verbose]}} {{path/to/file.ext}}`

- ضبط صفحه به مدت یک دقیقه:

`byzanz-record {{[-d|--duration]}} 60 {{path/to/file.ext}}`

- شروع ضبط با ۱۰ ثانیه تأخیر:

`byzanz-record --delay 10 {{path/to/file.ext}}`
