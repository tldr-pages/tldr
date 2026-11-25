# asusctl

> کنترل قابلیت‌های مختلف لپ‌تاپ‌های ASUS در لینوکس.
> اطلاعات بیشتر: <https://github.com/OpenGamingCollective/asusctl>.

- نمایش پروفایل فعلی:

`asusctl profile get`

- فهرست کردن پروفایل‌های موجود:

`asusctl profile list`

- تنظیم پروفایل عملکرد فعال:

`asusctl profile set performance`

- تنظیم روشنایی چراغ صفحه‌کلید:

`asusctl leds set {{off|low|med|high}}`

- تنظیم محدودیت شارژ باتری:

`asusctl battery limit {{80}}`

- نمایش محدودیت فعلی شارژ باتری:

`asusctl battery info`

- دریافت پروفایل‌های فعال فن:

`asusctl fan-curve --get-enabled`

- نمایش اطلاعات سیستم و قابلیت‌های پشتیبانی‌شده:

`asusctl info --show-supported`
