# openssl req

> أمر OpenSSL لإدارة طلبات توقيع الشهادات PKCS#10.
> لمزيد من التفاصيل: <https://www.openssl.org/docs/manmaster/man1/openssl-req.html>.

- إنشاء طلب توقيع شهادة لإرساله إلى جهة تصديق:

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- إنشاء شهادة موقعة ذاتيًا وزوج مفاتيح مقابلة، وحفظهما في ملف:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
