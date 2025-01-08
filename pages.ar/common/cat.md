# cat

> طباعة وسلسلة الملفات.
> لمزيد من التفاصيل: <https://manned.org/cat.1posix>.

- طباعة محتوي ملف إلى `stdout`:

`cat {{path/to/file}}`

- دمج عدة ملفات في ملف إخراج:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- إلحاق عدة ملفات بملف إخراج:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- نسخ محتويات ملف إلى ملف إخراج دون استخدام الذاكرة المؤقتة:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- كتابة `stdin` إلى ملف:

`cat - > {{path/to/file}}`
