# pvck

> بررسی و تعمیر فرادادهٔ LVM در حجم‌های فیزیکی.
> اطلاعات بیشتر: <https://manned.org/pvck>.

- چاپ سربرگ‌ها و ساختارهای LVM روی دیسک (برچسب، سربرگ PV، سربرگ MDA، ناحیهٔ فراداده):

`sudo pvck {{/dev/sdXN}} --dump headers`

- چاپ متن فرادادهٔ فعلی VG:

`sudo pvck {{/dev/sdXN}} --dump metadata`

- فهرست کردن همهٔ نسخه‌های فرادادهٔ یافت‌شده در ناحیهٔ فراداده:

`sudo pvck {{/dev/sdXN}} --dump metadata_all`

- جست‌وجوی محل‌های رایج برای فراداده در صورت احتمال خرابی سربرگ‌ها و ذخیرهٔ آن در فایل:

`sudo pvck {{/dev/sdXN}} --dump metadata_search {{[-f|--file]}} {{path/to/metadata.txt}}`

- انتخاب ناحیهٔ دوم فراداده (mda2) هنگام چاپ فراداده:

`sudo pvck {{/dev/sdXN}} --dump metadata --settings "mda_num=2"`

- تعمیر سربرگ‌ها و فراداده با استفاده از فایل ورودی فراداده (با احتیاط استفاده کنید):

`sudo pvck {{/dev/sdXN}} --repair {{[-f|--file]}} {{path/to/metadata_file}}`

- تعمیر فقط سربرگ PV و سربرگ برچسب:

`sudo pvck {{/dev/sdXN}} --repairtype pv_header`
