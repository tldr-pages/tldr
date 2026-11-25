# tracepath

> ردیابی مسیر به میزبان شبکه و کشف MTU در طول مسیر.
> اطلاعات بیشتر: <https://manned.org/tracepath>.

- ردیابی مسیر به میزبان با پورت مقصد مشخص:

`tracepath -p {{33434}} {{host}}`

- تعیین پورت مقصد اولیه، مفید با تنظیمات غیراستاندارد دیوار آتش:

`tracepath -p {{destination_port}} {{host}}`

- چاپ نام میزبان‌ها و آدرس‌های عددی IP:

`tracepath -b {{host}}`

- تعیین حداکثر TTL (تعداد گام‌ها):

`tracepath -m {{max_hops}} {{host}}`

- تعیین طول اولیهٔ بسته (پیش‌فرض ۶۵۵۳۵ برای IPv4 و ۱۲۸۰۰۰ برای IPv6):

`tracepath -l {{packet_length}} {{host}}`

- استفاده فقط از آدرس‌های IPv6:

`tracepath -6 {{host}}`
