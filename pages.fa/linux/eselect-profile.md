# eselect profile

> ماژول `eselect` برای مدیریت پیوند نمادین `/etc/portage/make.profile` که پروفایل سیستم را تعیین می‌کند.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eselect#Profile>.

- فهرست کردن مقصدهای موجود پیوند نمادین پروفایل همراه با شمارهٔ آن‌ها:

`eselect profile list`

- تنظیم پیوند نمادین `/etc/portage/make.profile` با نام یا شماره از دستور `list`:

`eselect profile set {{name|number}}`

- نمایش پروفایل فعلی سیستم:

`eselect profile show`
