# exec

> تنفيذ أمر دون إنشاء عملية فرعية.
> لمزيد من التفاصيل: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- تنفيذ أمر محدد:

`exec {{command -with -flags}}`

- تنفيذ أمر ضمن بيئة فارغة (تقريبًا):

`exec -c {{command -with -flags}}`

- تنفيذ أمر عبر login shell:

`exec -l {{command -with -flags}}`

- تنفيذ أمر بإسم مختلف:

`exec -a {{name}} {{command -with -flags}}`
