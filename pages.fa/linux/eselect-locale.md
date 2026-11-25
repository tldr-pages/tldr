# eselect locale

> ماژول `eselect` برای مدیریت متغیر محیطی `$LANG` که زبان سیستم را تنظیم می‌کند.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eselect#Locale>.

- فهرست کردن تنظیمات محلی موجود:

`eselect locale list`

- تنظیم متغیر محیطی `$LANG` در `/etc/profile.env` با نام یا شماره از دستور `list`:

`eselect locale set {{name|index}}`

- نمایش مقدار `$LANG` در `/etc/profile.env`:

`eselect locale show`
