# xml pyx

> একটি XML ডকুমেন্টকে PYX (ESIS - ISO 8879) ফরম্যাটে রূপান্তর করুন।
> আরও তথ্য পাবেন: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>।

- একটি XML ডকুমেন্টকে PYX ফরম্যাটে রূপান্তর করুন:

`xml pyx {{path/to/input.xml|URI}} > {{path/to/output.pyx}}`

- `stdin` থেকে একটি XML ডকুমেন্টকে PYX ফরম্যাটে রূপান্তর করুন:

`cat {{path/to/input.xml}} | xml pyx > {{path/to/output.pyx}}`

- সাহায্য প্রদর্শন করুন:

`xml pyx --help`
