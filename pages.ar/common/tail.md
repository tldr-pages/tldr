# tail

> عرض الجزء الأخير من ملف.
> انظر أيضًا: `head`.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- عرض آخر 'عدد' من الأسطر في ملف:

`tail {{[-n|--lines]}} {{count}} {{path/to/file}}`

- طباعة محتوى ملف بدءًا من سطر معين:

`tail {{[-n|--lines]}} +{{count}} {{path/to/file}}`

- طباعة عدد معين من البايتات من نهاية ملف معين:

`tail {{[-c|--bytes]}} {{count}} {{path/to/file}}`

- طباعة آخر الأسطر من ملف معين والاستمرار في قراءته حتى الضغط على `<Ctrl c>`:

`tail {{[-f|--follow]}} {{path/to/file}}`

- الاستمرار في قراءة الملف حتى الضغط على `<Ctrl c>`، حتى لو كان غير متاح:

`tail {{[-F|--retry --follow]}} {{path/to/file}}`

- عرض آخر 'عدد' من الأسطر في 'ملف' وتحديث العرض كل 'عدد' من الثواني:

`tail {{[-n|--lines]}} {{count}} {{[-s|--sleep-interval]}} {{seconds}} {{[-f|--follow]}} {{path/to/file}}`
