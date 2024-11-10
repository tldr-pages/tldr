# del

> حذف ملف واحد او مجموعه من الملفات.
> وهو الاسم المستعار للامر `Remove-Item`.
> هذه الوثائق تستند إلى إصدار سطر الأوامر (`cmd`) من `del`.
> لمزيد من التفاصيل: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- اعرض التوثيقات للأمر الأصلي:

`tldr remove-item`

- حذف ملف او أكثر او حذف التطابق مع أنماط:

`del {{file_pattern1 file_pattern2 ...}}`

- التأكيد قبل الحذف:

`del {{file_pattern}} /p`

- حذف ملفات القراءة فقط:

`del {{file_pattern}} /f`

- حذف الملفات الموجودة في المجلد الحالي وأيضًا الملفات الفرعية:

`del {{file_pattern}} /s`

- لا تطلب التأكيد عند حذف الملفات بناءً على محدد عام:

`del {{file_pattern}} /q`

- عرض المساعدة وقائمة السمات المتاحة:

`del /?`

- حذف ملف اعتمادا على محدد معين:

`del {{file_pattern}} /a {{attribute}}`
