# uv

> مدير حزم ومشاريع سريع للغة بايثون.
> بعض الأوامر الفرعية مثل `tool` و `python` لديها توثيق خاص بها.
> لمزيد من التفاصيل: <https://docs.astral.sh/uv/reference/cli>.

- إنشاء مشروع بايثون جديد في المجلد الحالي:

`uv init`

- إنشاء مشروع بايثون جديد في المسار المحدد:

`uv init {{path/to/directory}}`

- إضافة تبعية جديدة إلى المشروع:

`uv add {{package}}`

- إزالة تبعية من المشروع:

`uv remove {{package}}`

- تشغيل سكربت داخل بيئة المشروع:

`uv run {{path/to/script.py}}`

- تشغيل أمر داخل بيئة المشروع:

`uv run {{command}}`

- تحديث بيئة المشروع من `pyproject.toml`:

`uv sync`

- إنشاء ملف تأمين (lock file) لتبعيات المشروع:

`uv lock`
