# find

> البحث عن الملفات أو المُجَلَّدات داخل فروع مُجَلَّد، بشكل متكرر.
> انظر أيضًا: `fd`.
> لمزيد من التفاصيل: <https://manned.org/find>.

- البحث عن الملفات حسب الامتداد:

`find {{path/to/directory}} -name '{{*.ext}}'`

- البحث عن الملفات المطابقة لأنماط مسار/اسم متعددة:

`find {{path/to/directory}} -path '{{*/path/*/*.ext}}' -or -name '{{*pattern*}}'`

- البحث عن المُجَلَّدات المطابقة لاسم معين، مع تجاهل حالة الأحرف سواء أكانت صغيرة او كبيرة:

`find {{path/to/directory}} -type d -iname '{{*lib*}}'`

- البحث عن الملفات المطابقة لنمط معين، مع استثناء مسارات محددة:

`find {{path/to/directory}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- البحث عن الملفات التي تطابق نطاق حجم معين، مع تقييد العمق التكراري إلى "1":

`find {{path/to/directory}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- تنفيذ أمر لكل ملف (استخدم `{}` داخل الأمر للوصول إلى اسم الملف):

`find {{path/to/directory}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- البحث عن جميع الملفات المعدلة اليوم وتمرير النتائج إلى أمر واحد كوسيطات:

`find {{path/to/directory}} -daystart -mtime {{-1}} -exec {{tar -cvf archive.tar}} {} \+`

- البحث عن الملفات أو المُجَلَّدات الفارغة وحذفها مع عرض التفاصيل:

`find {{path/to/directory}} -type {{f|d}} -empty -delete -print`
