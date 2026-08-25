# echo

> طباعة نص أو قيمة متغير في الـ terminal.
> انظر أيضًا: `printf`.
> لمزيد من التفاصيل: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- طباعة نص على الشاشة. ملاحظة: علامات الاقتباس اختيارية:

`echo "{{Hello World}}"`

- طباعة نص يتضمن قيمة متغير بيئة:

`echo "{{My path is $PATH}}"`

- طباعة نص دون إضافة سطر جديد في النهاية:

`echo -n "{{Hello World}}"`

- إضافة نص إلى نهاية ملف:

`echo "{{Hello World}}" >> {{file.txt}}`

- تفعيل تفسير الرموز الخاصة مثل `\t` للجدولة و`\n` للسطر الجديد:

`echo -e "{{Column 1\tColumn 2}}"`

- عرض رمز الخروج للأمر السابق (في Windows استخدم `echo %errorlevel%`، وفي PowerShell `$lastexitcode`):

`echo $?`

- توجيه نص إلى مدخل برنامج آخر:

`echo "{{Hello World}}" | {{program}}`
