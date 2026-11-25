# bspc

> پیکربندی و کنترل `bspwm` و مدیریت گره‌ها، میزکارها، نمایشگرها و موارد دیگر.
> همچنین ببینید: `bspwm`.
> اطلاعات بیشتر: <https://github.com/baskerville/bspwm/blob/master/doc/bspwm.1.asciidoc>.

- تعریف دو میزکار مجازی:

`bspc monitor {{[-d|--reset-desktops]}} {{desktop_name1}} {{desktop_name2}}`

- قرار دادن تمرکز روی میزکار مشخص:

`bspc desktop {{[-f|--focus]}} {{number}}`

- بستن پنجره‌هایی که ریشهٔ آن‌ها گره انتخاب‌شده است:

`bspc node {{[-c|--close]}}`

- فرستادن گره انتخاب‌شده به میزکار مشخص:

`bspc node {{[-d|--to-desktop]}} {{number}}`

- تغییر وضعیت حالت تمام‌صفحه برای گره انتخاب‌شده:

`bspc node {{[-t|--state]}} ~fullscreen`

- تنظیم مقدار یک تنظیم مشخص:

`bspc config {{setting_name}} {{value}}`
