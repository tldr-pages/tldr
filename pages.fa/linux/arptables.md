# arptables

> مدیریت قواعد پالایش ARP با استفاده از پشتیبان `nftables`.
> بخشی از مجموعهٔ `xtables-nft` برای پالایش بسته‌های ARP است.
> اطلاعات بیشتر: <https://manned.org/arptables>.

- فهرست کردن همهٔ قواعد ARP در جدول پالایش:

`sudo arptables {{[-L|--list]}}`

- افزودن یک قاعده برای دور انداختن بسته‌های ARP از یک آدرس IP مشخص:

`sudo arptables {{[-A|--append]}} INPUT {{[-s|--source-ip]}} {{192.168.0.1}} {{[-j|--jump]}} DROP`

- حذف یک قاعدهٔ مشخص از زنجیرهٔ INPUT با شمارهٔ قاعده:

`sudo arptables {{[-D|--delete]}} INPUT {{rule_number}}`

- پاک کردن همهٔ قواعد در جدول پالایش:

`sudo arptables {{[-F|--flush]}}`

- تنظیم سیاست پیش‌فرض زنجیرهٔ OUTPUT روی ACCEPT:

`sudo arptables {{[-P|--policy]}} OUTPUT ACCEPT`

- ذخیرهٔ قواعد فعلی ARP در یک فایل:

`sudo arptables-save >{{path/to/file}}`
