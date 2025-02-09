# gpg

> برنامج GNU Privacy Guard.
> راجع `gpg2` للحصول على الإصدار الثاني من GNU Privacy Guard. تقوم معظم أنظمة التشغيل بربط `gpg` بـ `gpg2`.
> لمزيد من التفاصيل: <https://gnupg.org>.

- إنشاء مفتاح GPG عام وخاص بطريقة تفاعلية:

`gpg --full-generate-key`

- توقيع الملف `doc.txt` دون تشفير (يتم حفظ الإخراج في ملف `doc.txt.asc`):

`gpg --clearsign {{doc.txt}}`

- تشفير وتوقيع الملف `doc.txt` للمستخدمين alice@example.com و bob@example.com (يتم حفظ الإخراج في ملف `doc.txt.gpg`):

`gpg --encrypt --sign --recipient {{alice@example.com}} --recipient {{bob@example.com}} {{doc.txt}}`

- تشفير `doc.txt` باستخدام كلمة مرور فقط (يتم حفظ الإخراج في ملف `doc.txt.gpg`):

`gpg --symmetric {{doc.txt}}`

- فك تشفير `doc.txt.gpg` (يتم عرض الإخراج على `stdout`):

`gpg --decrypt {{doc.txt.gpg}}`

- استيراد مفتاح عام:

`gpg --import {{public.gpg}}`

- تصدير المفتاح العام للمستخدم alice@example.com (يتم عرض الإخراج على `stdout`):

`gpg --export --armor {{alice@example.com}}`

- تصدير المفتاح الخاص للمستخدم alice@example.com (يتم عرض الإخراج على `stdout`):

`gpg --export-secret-keys --armor {{alice@example.com}}`
