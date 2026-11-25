# avahi-resolve

> تبدیل نام میزبان‌ها و آدرس‌های IP به یکدیگر.
> اطلاعات بیشتر: <https://manned.org/avahi-resolve>.

- تبدیل نام یک سرویس محلی به آدرس IPv4 آن:

`avahi-resolve -4 {{[-n|--name]}} {{service.local}}`

- تبدیل یک IP به نام میزبان با خروجی مفصل:

`avahi-resolve {{[-v|--verbose]}} {{[-a|--address]}} {{ip_address}}`
