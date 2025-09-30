# shred

> الكتابة فوق الملفات لحذف البيانات بشكل آمن.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html>.

- الكتابة فوق ملف:

`shred {{path/to/file}}`

- الكتابة فوق ملف وعرض التقدم على الشاشة:

`shred {{-v|--verbose}} {{path/to/file}}`

- الكتابة فوق ملف وترك أصفار بدلاً من البيانات العشوائية:

`shred {{-z|--zero}} {{path/to/file}}`

- الكتابة فوق ملف عددًا معينًا من المرات:

`shred {{-n|--iterations}} {{25}} {{path/to/file}}`

- الكتابة فوق ملف ثم إزالته:

`shred --remove {{path/to/file}}`

- الكتابة فوق ملف 100 مرة، إضافة كتابة نهائية بالأصفار، حذفه بعد الكتابة وعرض تقدم العملية بشكل مفصل:

`shred {{-vzun|--verbose --zero -u --iterations}} 100 {{path/to/file}}`
