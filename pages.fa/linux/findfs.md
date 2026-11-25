# findfs

> یافتن سیستم فایل بر اساس برچسب یا UUID.
> اطلاعات بیشتر: <https://manned.org/findfs>.

- جست‌وجوی دستگاه‌های بلوکی بر اساس برچسب سیستم فایل:

`findfs LABEL={{label}}`

- جست‌وجو بر اساس UUID سیستم فایل:

`findfs UUID={{uuid}}`

- جست‌وجو بر اساس برچسب پارتیشن (جدول پارتیشن GPT یا MAC):

`findfs PARTLABEL={{partition_label}}`

- جست‌وجو بر اساس UUID پارتیشن (فقط جدول پارتیشن GPT):

`findfs PARTUUID={{partition_uuid}}`
