# stat

> عرض معلومات عن الملف ونظام الملفات.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- عرض خصائص ملف معين مثل الحجم، الأذونات، تواريخ الإنشاء والوصول، وغيرها:

`stat {{path/to/file}}`

- عرض خصائص ملف معين مثل الحجم، الأذونات، تواريخ الإنشاء والوصول، وغيرها بدون تسميات:

`stat {{-t|--terse}} {{path/to/file}}`

- عرض معلومات عن نظام الملفات حيث يوجد ملف معين:

`stat {{-f|--file-system}} {{path/to/file}}`

- عرض أذونات الملف بصيغة ثُمانية فقط:

`stat {{-c|--format}} "%a %n" {{path/to/file}}`

- عرض مالك الملف والمجموعة التابعة له:

`stat {{-c|--format}} "%U %G" {{path/to/file}}`

- عرض حجم ملف معين بالبايت:

`stat {{-c|--format}} "%s %n" {{path/to/file}}`
