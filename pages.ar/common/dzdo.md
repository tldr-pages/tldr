# dzdo

> تنفيذ أوامر بامتيازات مرتفعة كمستخدم الجذر (root) أو كمستخدم آخر عبر أدوار Active Directory.
> مشابه لـ `sudo` ولكنه مدمج مع Delinea؛ ويدعم إضافة Ansible become.
> لمزيد من التفاصيل: <https://docs.delinea.com/online-help/server-suite/commandref/centrify-command-reference-2025.pdf#page=102>.

- تشغيل أمر بامتيازات مرتفعة:

`dzdo {{command}}`

- تشغيل أمر كمستخدم معين:

`dzdo -u {{username}} {{command}}`

- تعديل ملف بامتيازات مرتفعة باستخدام المحرر الافتراضي:

`dzdo -e {{path/to/file}}`

- تشغيل صدفة تسجيل دخول تفاعلية بامتيازات مرتفعة:

`dzdo -i`

- تشغيل الصدفة الافتراضية بامتيازات مرتفعة:

`dzdo -s`

- عرض الأوامر المسموح بها للمستخدم الحالي:

`dzdo -l`

- التحقق من صحة الطابع الزمني للمصادقة وتحديثه:

`dzdo -v`

- عرض الإصدار:

`dzdo -V`
