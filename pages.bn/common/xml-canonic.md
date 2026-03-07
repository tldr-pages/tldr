# xml canonic

> XML ডকুমেন্টকে ক্যানোনিকাল বানিয়ে ফেলুন।
> আরও তথ্য পাবেন: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139560880>।

- কমেন্ট সংরক্ষণ করে একটি XML ডকুমেন্টকে ক্যানোনিকাল তৈরি করুন:

`xml {{[c14n|canonic]}} {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- কমেন্ট সরিয়ে একটি XML ডকুমেন্টকে ক্যানোনিকাল তৈরি করুন:

`xml {{[c14n|canonic]}} --without-comments {{path/to/input.xml|URI}} > {{path/to/output.xml}}`

- কমেন্ট সংরক্ষণ করে, একটি ফাইল থেকে XPATH ব্যবহার করে XML এক্সক্লুসিভ ক্যানোনিকাল তৈরি করুন:

`xml {{[c14n|canonic]}} --exc-with-comments {{path/to/input.xml|URI}} {{path/to/c14n.xpath}}`

- সাহায্য প্রদর্শন করুন:

`xml {{[c14n|canonic]}} --help`
