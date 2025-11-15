# mtr

> أداة Matt's Traceroute: تجمع بين traceroute و ping.
> لمزيد من التفاصيل: <https://manned.org/mtr>.

- تتبع المسار إلى مضيف وإرسال حزم ping مستمرة لجميع النقاط الوسيطة:

`mtr {{example.com}}`

- تعطيل تعيين عناوين IP وأسماء المضيفين:

`mtr {{[-n|--no-dns]}} {{example.com}}`

- عرض المخرجات بعد إرسال 10 حزم ping لكل نقطة:

`mtr {{[-w|--report-wide]}} {{example.com}}`

- فرض استخدام IPv4 أو IPv6:

`mtr -4 {{example.com}}`

- الانتظار لوقت محدد (بالثواني) قبل إرسال حزمة أخرى إلى نفس النقطة:

`mtr {{[-i|--interval]}} {{10}} {{example.com}}`

- عرض رقم النظام المستقل (ASN) لكل نقطة:

`mtr {{[-z|--aslookup]}} {{example.com}}`

- عرض كل من عنوان IP والاسم العكسي لـ DNS:

`mtr {{[-b|--show-ips]}} {{example.com}}`
