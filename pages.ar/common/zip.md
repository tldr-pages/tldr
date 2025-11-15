# zip

> أداة لضغط وحزم الملفات في أرشيف Zip.
> انظر أيضًا: `unzip`.
> لمزيد من التفاصيل: <https://manned.org/zip>.

- إضافة ملفات/مجلدات إلى أرشيف محدد ([r]بشكل متكرر):

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- إزالة ملفات/مجلدات من أرشيف محدد ([d]حذف):

`zip {{[-d|--delete]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- أرشفة ملفات/مجلدات مع [x]استثناء عناصر معينة:

`zip {{[-r|--recurse-paths]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{[-x|--exclude]}} {{path/to/excluded_files_or_directories}}`

- أرشفة ملفات/مجلدات مع مستوى ضغط محدد (`0` - الأقل، `9` - الأعلى):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- إنشاء أرشيف [e]مشفر باستخدام كلمة مرور محددة:

`zip {{[-re|--recurse-paths --encrypt]}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- أرشفة ملفات/مجلدات في أرشيف Zip مقسم[s] إلى أجزاء متعددة (مثل أجزاء بحجم 3 جيجابايت):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{path/to/compressed.zip}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- طباعة محتويات أرشيف محدد:

`zip {{[-sf|--split-size --freshen]}} {{path/to/compressed.zip}}`
