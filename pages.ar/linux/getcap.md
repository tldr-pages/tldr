# getcap

> أمر لعرض اسم وصلاحيات كل ملف محدد.
> لمزيد من التفاصيل: <https://manned.org/getcap>.

- الحصول على الصلاحيات للملفات المحددة:

`getcap {{path/to/file1 path/to/file2 ...}}`

- (Recursive) الحصول على الصلاحيات لجميع الملفات داخل المجلدات المحددة بشكل متكرر:

`getcap -r {{path/to/directory1 path/to/directory2 ...}}`

- عرض جميع الإدخالات التي تم البحث عنها حتى لو لم يتم تعيين أي صلاحيات:

`getcap -v {{path/to/file1 path/to/file2 ...}}`
