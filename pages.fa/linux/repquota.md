# repquota

> نمایش خلاصهٔ سهمیه‌های فایل موجود برای فایل‌سیستم.
> اطلاعات بیشتر: <https://manned.org/repquota>.

- گزارش آمار همهٔ سهمیه‌های در حال استفاده:

`sudo repquota {{[-a|--all]}}`

- گزارش آمار سهمیهٔ همهٔ کاربران، حتی کسانی که از سهمیه استفاده نمی‌کنند:

`sudo repquota {{[-v|--verbose]}} {{filesystem}}`

- گزارش سهمیهٔ فقط کاربران:

`repquota {{[-u|--user]}} {{filesystem}}`

- گزارش سهمیهٔ فقط گروه‌ها:

`sudo repquota {{[-g|--group]}} {{filesystem}}`

- گزارش سهمیهٔ مصرف‌شده و محدودیت‌ها در قالب خوانا برای انسان:

`sudo repquota {{[-s|--human-readable]}} {{filesystem}}`

- گزارش همهٔ سهمیه‌های کاربران و گروه‌ها در قالب خوانا برای انسان:

`sudo repquota {{[-augs|--all --user --group --human-readable]}}`
