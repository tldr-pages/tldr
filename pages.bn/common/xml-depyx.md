# xml depyx

> একটি PYX (ESIS - ISO 8879) ডকুমেন্টকে XML ফরম্যাটে রূপান্তর করুন।
> আরও তথ্য পাবেন: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>।

- একটি PYX (ESIS - ISO 8879) ডকুমেন্টকে XML ফরম্যাটে রূপান্তর করুন:

`xml {{[p2x|depyx]}} {{path/to/input.pyx|URI}} > {{path/to/output.xml}}`

- `stdin` থেকে একটি PYX ডকুমেন্টকে XML ফরম্যাটে রূপান্তর করুন:

`cat {{path/to/input.pyx}} | xml {{[p2x|depyx]}} > {{path/to/output.xml}}`

- সাহায্য প্রদর্শন করুন:

`xml {{[p2x|depyx]}} --help`
