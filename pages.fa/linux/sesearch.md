# sesearch

> جست‌وجوی قوانین سیاست SELinux.
> بخشی از بستهٔ `setools`.
> همچنین ببینید: `semodule`.
> اطلاعات بیشتر: <https://manned.org/sesearch>.

- جست‌وجوی همهٔ قوانین اجازه:

`sesearch --allow`

- جست‌وجوی قوانین مرتبط با نوع مشخص:

`sesearch --allow {{[-t|--target]}} {{type_name}}`

- جست‌وجوی قوانین مرتبط با نوع مبدأ مشخص:

`sesearch --allow {{[-s|--source]}} {{source_type}}`

- جست‌وجوی قوانینی که رده و مجوز مشخص را مجاز می‌کنند:

`sesearch --allow {{[-c|--class]}} {{class_name}} {{[-p|--perm]}} {{permission}}`

- جست‌وجوی قوانین با نوع مقصد و ردهٔ مشخص:

`sesearch --allow {{[-t|--target]}} {{type_name}} {{[-c|--class]}} {{class_name}}`

- نمایش اطلاعات مفصل‌تر دربارهٔ قوانین مطابق:

`sesearch --allow {{[-t|--target]}} {{type_name}} {{[-v|--verbose]}}`
