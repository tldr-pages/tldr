# wc

> عدّ الأسطر والكلمات والبايتات.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- عدّ جميع الأسطر في ملف:

`wc {{[-l|--lines]}} {{path/to/file}}`

- عدّ جميع الكلمات في ملف:

`wc {{[-w|--words]}} {{path/to/file}}`

- عدّ جميع البايتات في ملف:

`wc {{[-c|--bytes]}} {{path/to/file}}`

- عدّ جميع الأحرف في ملف (مع أخذ الأحرف متعددة البايتات في الاعتبار مثل الحروف العربية):

`wc {{[-m|--chars]}} {{path/to/file}}`

- عدّ جميع الأسطر والكلمات والبايتات من `stdin`:

`{{find .}} | wc`

- حساب طول أطول سطر بعدد الأحرف:

`wc {{[-L|--max-line-length]}} {{path/to/file}}`
