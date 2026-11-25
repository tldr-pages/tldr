# po4a-updatepo

> به‌روزرسانی ترجمهٔ مستندات (در قالب PO).
> اطلاعات بیشتر: <https://www.po4a.org/man/man1/po4a-updatepo.1.php>.

- به‌روزرسانی فایل PO بر اساس تغییر فایل مبدأ آن:

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- فهرست کردن قالب‌های موجود:

`po4a-updatepo --help-format`

- به‌روزرسانی چند فایل PO بر اساس تغییر فایل مبدأ آن‌ها:

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/po1.po}} --po {{path/to/po2.po}}`
