# avahi-browse

> نمایش سرویس‌ها و میزبان‌های معرفی‌شده در شبکهٔ محلی از طریق mDNS/DNS-SD.
> Avahi با Bonjour (Zeroconf) موجود در دستگاه‌های اپل سازگار است.
> اطلاعات بیشتر: <https://manned.org/avahi-browse>.

- فهرست کردن سرویس‌های موجود در شبکهٔ محلی همراه با آدرس‌ها و درگاه‌های آن‌ها، با نادیده گرفتن سرویس‌های دستگاه محلی:

`avahi-browse {{[-a|--all]}} {{[-r|--resolve]}} {{[-l|--ignore-local]}}`

- فهرست کردن سریع سرویس‌های شبکهٔ محلی در قالب SSV برای اسکریپت‌ها:

`avahi-browse {{[-a|--all]}} {{[-t|--terminate]}} {{[-p|--parsable]}}`

- فهرست کردن دامنه‌های موجود در شبکهٔ مجاور:

`avahi-browse {{[-D|--browse-domains]}}`

- محدود کردن جست‌وجو به یک دامنهٔ مشخص:

`avahi-browse {{[-a|--all]}} --domain={{domain}}`
