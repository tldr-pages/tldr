# host

> البحث في خادم أسماء النطاقات (DNS).
> لمزيد من التفاصيل: <https://manned.org/host>.

- البحث عن سجلات A و AAAA و MX لنطاق معين:

`host {{domain}}`

- البحث عن نوع معين من السجلات (مثل CNAME أو TXT) لنطاق معين:

`host -t {{field}} {{domain}}`

- البحث العكسي عن عنوان IP:

`host {{ip_address}}`

- تحديد خادم DNS بديل للاستعلام:

`host {{domain}} {{8.8.8.8}}`
