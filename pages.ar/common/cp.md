# cp

> نسخ الملفات والمجلدات.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- نسخ ملف إلى موقع آخر:

`cp {{path/to/source_file}} {{path/to/target_file}}`

- نسخ ملف داخل مجلد مع الاحتفاظ باسمه:

`cp {{path/to/source_file}} {{path/to/target_parent_directory}}`

- نسخ مجلد بالكامل بما يشمل المجلدات الفرعية (إن وُجد المجلد الهدف، يُنسخ المصدر بداخله):

`cp {{[-r|--recursive]}} {{path/to/source_directory}} {{path/to/target_directory}}`

- نسخ مجلد بالكامل مع عرض اسم كل ملف أثناء نسخه:

`cp {{[-vr|--verbose --recursive]}} {{path/to/source_directory}} {{path/to/target_directory}}`

- نسخ عدة ملفات إلى مجلد في آنٍ واحد:

`cp {{[-t|--target-directory]}} {{path/to/destination_directory}} {{path/to/file1 path/to/file2 ...}}`

- نسخ جميع ملفات بامتداد معين مع طلب تأكيد عند الكتابة فوق ملف موجود:

`cp {{[-i|--interactive]}} {{*.ext}} {{path/to/target_directory}}`

- اتباع الروابط الرمزية قبل النسخ:

`cp {{[-L|--dereference]}} {{link}} {{path/to/target_directory}}`

- الحفاظ على هيكل المسار الكامل أثناء النسخ، وإنشاء المجلدات الوسيطة عند الحاجة:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
