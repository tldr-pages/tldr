# abrt-cli
> أداة سطر أوامر للإبلاغ التلقائي عن الأعطال.
> تُستخدم لعرض وتحليل وإرسال تقارير الكراشات والمشاكل.
> لمزيد من التفاصيل: <https://abrt.readthedocs.io/>.

- عرض جميع المشاكل المكتشفة:
`abrt-cli list`

- عرض تفاصيل مشكلة معيّنة:
`abrt-cli info {{problem_id}}`

- حذف تقرير مشكلة:
`abrt-cli remove {{problem_id}}`

- حذف جميع التقارير المخزنة:
`abrt-cli remove --all`

- إرسال تقرير مشكلة:
`abrt-cli report {{problem_id}}`

- تحليل تقرير كراش:
`abrt-cli analyze {{problem_id}}`

- إعادة تحليل الكراش لأغراض التصحيح:
`abrt-cli retrace {{problem_id}}`

- مراقبة الأعطال الجديدة مباشرة:
`abrt-cli watch`

- عرض حالة خدمة ABRT:
`abrt-cli status`