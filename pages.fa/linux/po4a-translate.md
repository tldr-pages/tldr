# po4a-translate

> تبدیل مجدد فایل PO به قالب مستندات.
> فایل PO ارائه‌شده باید ترجمهٔ فایل POT تولیدشده توسط `po4a-gettextize` باشد.
> اطلاعات بیشتر: <https://www.po4a.org/man/man1/po4a-translate.1.php>.

- تبدیل مجدد فایل PO ترجمه‌شده به سند:

`po4a-translate --format {{text}} --master {{path/to/master.doc}} --po {{path/to/result.po}} --localized {{path/to/translated.txt}}`

- فهرست کردن همهٔ قالب‌های موجود:

`po4a-translate --help-format`
