# rmdir

> إزالة الدليل ومحتوياته.
> في PowerShell، هذا الأمر هو اسم مستعار لـ "إزالة العنصر". تعتمد هذه الوثائق على إصدار موجه الأوامر (`cmd`) من `rmdir`.
> مزيد من المعلومات: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- عرض وثائق أمر PowerShell المكافئ:

`tldr remove-item`

- إزالة دليل فارغ:

`rmdir {{path\to\directory}}`

- إزالة الدليل ومحتوياته بشكل متكرر:

`rmdir {{path\to\directory}} /s`

- إزالة الدليل ومحتوياته بشكل متكرر دون مطالبة:

`rmdir {{path\to\directory}} /s /q`
