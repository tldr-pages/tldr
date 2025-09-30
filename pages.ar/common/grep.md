# grep

> (Regular Expressions) البحث عن أنماط في الملفات باستخدام التعابير النمطية.
> لمزيد من التفاصيل: <https://www.gnu.org/software/grep/manual/grep.html>.

- البحث عن نمط داخل ملف:

`grep "{{search_pattern}}" {{path/to/file}}`

- البحث عن سلسلة نصية مطابقة تمامًا (تعطيل التعابير النمطية):

`grep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- البحث عن نمط في جميع الملفات داخل دليل بشكل متكرر، مع عرض أرقام الأسطر المطابقة، وتجاهل الملفات الثنائية:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{search_pattern}}" {{path/to/directory}}`

- استخدام التعابير النمطية الموسعة (يدعم `?`, `+`, `{}`, `()`, و `|`)، في وضع عدم التمييز بين الأحرف الكبيرة والصغيرة:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`

- طباعة 3 أسطر من السياق حول، قبل أو بعد كل تطابق:

`grep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- طباعة اسم الملف ورقم السطر لكل تطابق مع تمييز بالألوان:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- البحث عن الأسطر المطابقة لنمط معين، مع طباعة النص المطابق فقط:

`grep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- البحث في `stdin` عن الأسطر التي لا تطابق النمط:

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{search_pattern}}"`
