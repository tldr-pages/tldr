# am

> مدير الأنشطة في أندرويد.
> لمزيد من التفاصيل: <https://developer.android.com/tools/adb#am>.

- ابدأ نشاطا بتحديد اسم الحزمة/المكوّن بالكامل:

`am start -n {{com.android.settings/.Settings}}`

- ابدأ فعلا (action) ومرّر بيانات (data) له:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- ابدأ نشاطا يطابق فعلا (action) وفئة (category) معيّنة:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- حوّل Intent إلى URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
