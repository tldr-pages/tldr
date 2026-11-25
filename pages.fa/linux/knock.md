# knock

> کارخواه port knocking برای باز کردن پورت‌های مشخص در دیوار آتش.
> اطلاعات بیشتر: <https://manned.org/knock>.

- کوبیدن به پورت‌ها با پروتکل‌های مختلف:

`knock {{hostname}} {{portnumber}}:{{protocol}}`

- کوبیدن به پورت با UDP:

`knock {{[-u|--udp]}} {{hostname}} {{portnumber}}`

- اجبار استفاده از IPv4 یا IPv6:

`knock {{-4|-6}} {{hostname}} {{portnumber}}`

- نمایش خطاها و جزئیات اتصال:

`knock {{[-v|--verbose]}} {{hostname}} {{portnumber}}`
