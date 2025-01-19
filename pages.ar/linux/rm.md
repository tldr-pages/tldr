# rm

> يستخدم الأمر لحذف الملفات او المجلدات
> أنظر أيضًا: `rmdir`.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- حذف ملفات محددة:

`rm {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات محددة وتجاهل الملفات الغير موجودة:

`rm --force {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات محددة مع واجهة تفاعلية قبل اي حذف للتأكد:

`rm --interactive {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات محددة مع عرض تفاصيل حول كل عملية حذف:

`rm --verbose {{path/to/file1 path/to/file2 ...}}`

- حذف ملفات ومجلدات محددة بشكل تسلسلي:

`rm --recursive {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- حذف المجلدات الفارغة (هذه الطريقة تعتبر آمنة):

`rm --dir {{path/to/directory}}`
