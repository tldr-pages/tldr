# uuidparse

> تجزیهٔ شناسه‌های یکتای جهانی.
> همچنین ببینید: `uuidgen`.
> اطلاعات بیشتر: <https://manned.org/uuidparse>.

- تجزیهٔ UUIDهای مشخص با قالب خروجی جدولی:

`uuidparse {{uuid1 uuid2 ...}}`

- تجزیهٔ UUIDها از `stdin`:

`{{command}} | uuidparse`

- استفاده از قالب خروجی JSON:

`uuidparse {{[-J|--json]}} {{uuid1 uuid2 ...}}`

- چاپ نکردن خط سربرگ:

`uuidparse {{[-n|--noheadings]}} {{uuid1 uuid2 ...}}`

- استفاده از قالب خروجی خام:

`uuidparse {{[-r|--raw]}} {{uuid1 uuid2 ...}}`

- تعیین ستون‌های قابل چاپ از چهار ستون خروجی:

`uuidparse {{[-o|--output]}} {{UUID,VARIANT,TYPE,TIME}}`

- نمایش راهنما:

`uuidparse {{[-h|--help]}}`
