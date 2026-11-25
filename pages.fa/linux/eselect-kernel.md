# eselect kernel

> ماژول `eselect` برای مدیریت پیوند نمادین `/usr/src/linux`.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- فهرست کردن مقصدهای موجود پیوند نمادین هسته همراه با شمارهٔ آن‌ها:

`eselect kernel list`

- تنظیم پیوند نمادین `/usr/src/linux` با نام یا شماره از دستور `list`:

`eselect kernel set {{name|number}}`

- نمایش مقصد پیوند نمادین فعلی هسته:

`eselect kernel show`

- تنظیم پیوند نمادین هسته به هستهٔ در حال اجرا:

`eselect kernel update`
