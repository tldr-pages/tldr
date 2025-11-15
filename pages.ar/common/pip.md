# pip

> مدير الحزم الخاص بلغة بايثون.
> بعض الأوامر الفرعية مثل `install` لديها توثيق خاص بها.
> لمزيد من التفاصيل: <https://pip.pypa.io/en/stable/cli/pip/>.

- تثبيت حزمة (راجع `pip install` لمزيد من خيارات التثبيت):

`pip install {{package}}`

- تثبيت حزمة في مجلد المستخدم بدلاً من الموقع الافتراضي للنظام:

`pip install --user {{package}}`

- تحديث حزمة مثبتة:

`pip install {{[-U|--upgrade]}} {{package}}`

- إزالة تثبيت حزمة:

`pip uninstall {{package}}`

- حفظ قائمة الحزم المثبتة في ملف:

`pip freeze > {{requirements.txt}}`

- عرض معلومات عن حزمة مثبتة:

`pip show {{package}}`

- تثبيت الحزم من ملف متطلبات:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
