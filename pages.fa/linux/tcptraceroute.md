# tcptraceroute

> پیاده‌سازی traceroute با بسته‌های TCP.
> اطلاعات بیشتر: <https://manned.org/tcptraceroute>.

- ردیابی مسیر به میزبان:

`tcptraceroute {{host}}`

- تعیین پورت مقصد و طول بسته بر حسب بایت:

`tcptraceroute {{host}} {{destination_port}} {{packet_length}}`

- تعیین پورت مبدأ محلی و آدرس مبدأ:

`tcptraceroute {{host}} -p {{source_port}} -s {{source_address}}`

- تنظیم نخستین و حداکثر TTL:

`tcptraceroute {{host}} -f {{first_ttl}} -m {{max_ttl}}`

- تعیین زمان انتظار و تعداد پرس‌وجو در هر گام:

`tcptraceroute {{host}} -w {{wait_time}} -q {{number_of_queries}}`

- تعیین واسط:

`tcptraceroute {{host}} -i {{interface}}`
