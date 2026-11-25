# po4a-gettextize

> تبدیل فایل به فایل PO.
> اطلاعات بیشتر: <https://www.po4a.org/man/man1/po4a-gettextize.1.php>.

- تبدیل فایل متنی به فایل PO:

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- فهرست کردن همهٔ قالب‌های موجود:

`po4a-gettextize --help-format`

- تبدیل فایل متنی همراه با سند ترجمه‌شده به فایل PO (گزینهٔ `-l` را می‌توان چند بار ارائه کرد):

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --localized {{path/to/translated.txt}} --po {{path/to/result.po}}`
