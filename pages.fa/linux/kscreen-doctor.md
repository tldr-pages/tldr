# kscreen-doctor

> تغییر و تنظیم چیدمان صفحه‌نمایش.
> اطلاعات بیشتر: <https://invent.kde.org/plasma/libkscreen>.

- نمایش اطلاعات خروجی نمایشگر:

`kscreen-doctor {{[-o|--outputs]}}`

- تنظیم چرخش خروجی نمایشگر با شناسهٔ ۱ به سمت راست:

`kscreen-doctor output.1.rotation.right`

- تنظیم مقیاس خروجی نمایشگر با شناسهٔ `HDMI-2` به ۲ (۲۰۰٪):

`kscreen-doctor output.HDMI-2.scale.2`

- فعال کردن نمایشگر HDMI مشخص:

`kscreen-doctor output.{{HDMI-A-1}}.enable`

- غیرفعال کردن نمایشگر DisplayPort مشخص:

`kscreen-doctor output.{{DP-2}}.disable`

- تنظیم یک نمایشگر به‌عنوان نمایشگر اصلی:

`kscreen-doctor output.{{HDMI-A-1}}.primary`

- نمایش راهنما:

`kscreen-doctor {{[-h|--help]}}`
