# gcc

> معالجة مسبقة وتجميع ملفات مصدر C و C++، ثم تجميعها وربطها معًا.
> جزء من GCC (مجموعة مترجمات جنو).
> لمزيد من التفاصيل: <https://gcc.gnu.org/onlinedocs/gcc/>.

- ترجمة ملفات مصدر متعددة إلى ملف قابل للتنفيذ:

`gcc {{path/to/source1.c path/to/source2.c ...}} {{-o|--output}} {{path/to/output_executable}}`

- تفعيل عرض جميع الأخطاء والتحذيرات:

`gcc {{path/to/source.c}} -Wall {{-o|--output}} {{output_executable}}`

- عرض التحذيرات الشائعة، وإضافة رموز التصحيح إلى الإخراج، وتحسين الأداء دون التأثير على التصحيح:

`gcc {{path/to/source.c}} -Wall {{-g|--debug}} -Og {{-o|--output}} {{path/to/output_executable}}`

- تضمين مكتبات من مسار مختلف:

`gcc {{path/to/source.c}} {{-o|--output}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- ترجمة الكود المصدري إلى تعليمات لغة التجميع:

`gcc {{-S|--assemble}} {{path/to/source.c}}`

- ترجمة الكود المصدري إلى ملف كائن دون ربط:

`gcc {{-c|--compile}} {{path/to/source.c}}`

- تحسين البرنامج المترجم لزيادة الأداء:

`gcc {{path/to/source.c}} -O{{1|2|3|fast}} {{-o|--output}} {{path/to/output_executable}}`

- عرض الإصدار:

`gcc --version`
