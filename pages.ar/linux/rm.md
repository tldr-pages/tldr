# rm

> يستخدم الأمر لحذف الملفات او المجلدات
> أنظر أيضًا: `rmdir`.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- حذف ملفات محددة:

`rm {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات محددة وتجاهل الملفات الغير موجودة:

`rm {{[-f|--force]}} {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات محددة مع واجهة تفاعلية قبل اي حذف للتأكد:

`rm {{[-i|--interactive]}} {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات محددة مع عرض تفاصيل حول كل عملية حذف:

`rm {{[-v|--verbose]}} {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات ومجلدات محددة بشكل تسلسلي:

`rm {{[-r|--recursive]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- حذف المجلدات الفارغة (هذه الطريقة تعتبر آمنة):

`rm {{[-d|--dir]}} {{path/to/directory}}`
