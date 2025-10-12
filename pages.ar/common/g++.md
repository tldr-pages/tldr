# g++

> ترجمة ملفات مصدر C++.
> جزء من حزمة GCC (مجموعة مترجمات جنو).
> لمزيد من التفاصيل: <https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html>.

- ترجمة ملف أو عدة ملفات مصدر إلى ملف تنفيذي:

`g++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- إظهار جميع التحذيرات:

`g++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{path/to/output_executable}}`

- إظهار التحذيرات الشائعة، تضمين رموز التصحيح، وتحسين لا يؤثر في إزالة التصحيح:

`g++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- اختيار معيار اللغة المستهدف (C++98/C++11/C++14/C++17):

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{path/to/output_executable}}`

- تضمين مسارات للرؤوس والمكتبات والربط بمكتبة:

`g++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- ترجمة ثم ربط عدة ملفات مصدر على خطوتين:

`g++ {{[-c|--compile]}} {{path/to/source1.cpp path/to/source2.cpp ...}} && g++ {{[-o|--output]}} {{path/to/output_executable}} {{path/to/source1.o path/to/source2.o ...}}`

- تحسين الأداء عند الترجمة:

`g++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- عرض الإصدار:

`g++ --version`
