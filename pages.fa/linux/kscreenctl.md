# kscreenctl

> مدیریت خروجی‌های نمایشگر در KDE Plasma.
> همچنین : `kscreen-doctor`, `kscreen-console`.
> اطلاعات بیشتر: <https://invent.kde.org/plasma/kscreen>.

- فهرست کردن همهٔ خروجی‌های متصل:

`kscreenctl list-outputs`

- نمایش برچسب روی هر نمایشگر برای شناسایی نام اتصال‌دهنده‌ها:

`kscreenctl identify`

- نمایش اطلاعات خروجی مشخص (یا استفاده از `active-output` / `primary-output`):

`kscreenctl {{DP-1}}`

- تنظیم وضوح و نرخ نوسازی خروجی:

`kscreenctl {{DP-1}} set-mode 1920x1080@60`

- تنظیم مقیاس خروجی به ۲۰۰٪:

`kscreenctl {{DP-1}} set-scale 200%`

- قرار دادن یک خروجی در سمت راست خروجی دیگر:

`kscreenctl {{HDMI-A-1}} right-of {{DP-1}}`

- غیرفعال کردن خروجی مشخص:

`kscreenctl {{HDMI-A-1}} set-enabled false`

- خاموش کردن همهٔ خروجی‌ها از طریق سیگنال‌دهی مدیریت توان نمایشگر:

`kscreenctl off`
