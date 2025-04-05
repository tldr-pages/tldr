# mtr

> أداة Matt's Traceroute: تجمع بين traceroute و ping.
> لمزيد من التفاصيل: <https://www.bitwizard.nl/mtr/>.

- تتبع المسار إلى مضيف وإرسال حزم ping مستمرة لجميع النقاط الوسيطة:

`mtr {{example.com}}`

- تعطيل تعيين عناوين IP وأسماء المضيفين:

`mtr --no-dns {{example.com}}`

- عرض المخرجات بعد إرسال 10 حزم ping لكل نقطة:

`mtr --report-wide {{example.com}}`

- فرض استخدام IPv4 أو IPv6:

`mtr -4 {{example.com}}`

- الانتظار لوقت محدد (بالثواني) قبل إرسال حزمة أخرى إلى نفس النقطة:

`mtr --interval {{10}} {{example.com}}`

- عرض رقم النظام المستقل (ASN) لكل نقطة:

`mtr --aslookup {{example.com}}`

- عرض كل من عنوان IP والاسم العكسي لـ DNS:

`mtr --show-ips {{example.com}}`
