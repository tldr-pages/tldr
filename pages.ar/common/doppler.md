# doppler

> إدارة المتغيرات البيئية عبر بيئات مختلفة باستخدام Doppler.
> بعض الأوامر الفرعية مثل `run` و `secrets` تحتوي على وثائق استخدام خاصة بها.
> لمزيد من التفاصيل: <https://docs.doppler.com/docs/cli>.

- إعداد Doppler CLI في الدليل الحالي:

`doppler setup`

- إعداد مشروع Doppler والتكوين في الدليل الحالي:

`doppler setup`

- تشغيل أمر مع حقن الأسرار في البيئة:

`doppler run --command {{command}}`

- عرض قائمة المشاريع الخاصة بك:

`doppler projects`

- عرض الأسرار للمشروع الحالي:

`doppler secrets`

- فتح لوحة تحكم Doppler في المتصفح:

`doppler open`
