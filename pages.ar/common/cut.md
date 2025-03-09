# cut

> استخراج حقول من `stdin` أو من الملفات.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html>.

- طباعة نطاق [c]حرف/[f]حقل محدد من كل سطر:

`{{command}} | cut --{{characters|fields}} {{1|1,10|1-10|1-|-10}}`

- طباعة نطاق [f]حقل محدد من كل سطر باستخدام [d]فاصل معين:

`{{command}} | cut --delimiter "{{,}}" --fields {{1}}`

- طباعة نطاق [c]حرف معين من كل سطر في ملف محدد:

`cut --characters {{1}} {{path/to/file}}`

- طباعة [f]حقول محددة من أسطر منتهية بـ `NUL` (مثل الناتج من `find . -print0`) بدلاً من أسطر جديدة:

`{{command}} | cut --zero-terminated --fields {{1}}`
