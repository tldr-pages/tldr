# g++

> ترجمة ملفات مصدر C++.
> جزء من GCC (مجموعة مترجمات جنو).
> لمزيد من التفاصيل: <https://gcc.gnu.org>.

- ترجمة ملف مصدر إلى ملف تنفيذي ثنائي (Binary):

`g++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{-o|--output}} {{path/to/output_executable}}`

- تفعيل عرض جميع الأخطاء والتحذيرات:

`g++ {{path/to/source.cpp}} -Wall {{-o|--output}} {{output_executable}}`

- عرض التحذيرات الشائعة، وإضافة رموز التصحيح إلى الإخراج، وتحسين الأداء دون التأثير على التصحيح:

`g++ {{path/to/source.cpp}} -Wall {{-g|--debug}} -Og {{-o|--output}} {{path/to/output_executable}}`

- اختيار معيار لغة C++ للترجمة (C++98/C++11/C++14/C++17):

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} {{-o|--output}} {{path/to/output_executable}}`

- تضمين مكتبات تقع في مسار مختلف عن ملف المصدر:

`g++ {{path/to/source.cpp}} {{-o|--output}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- ترجمة وربط ملفات مصدر متعددة في ملف تنفيذي ثنائي (Binary):

`g++ {{-c|--compile}} {{path/to/source1.cpp path/to/source2.cpp ...}} && g++ {{-o|--output}} {{path/to/output_executable}} {{path/to/source1.o path/to/source2.o ...}}`

- تحسين البرنامج المترجم لزيادة الأداء:

`g++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{-o|--output}} {{path/to/output_executable}}`

- عرض الإصدار:

`g++ --version`
