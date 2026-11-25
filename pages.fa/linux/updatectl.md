# updatectl

> ابزار به‌روزرسانی سیستم.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/updatectl.html>.

- بررسی وجود به‌روزرسانی برای سیستم:

`updatectl check`

- به‌روزرسانی به جدیدترین نسخه:

`updatectl update`

- نمایش مقصدهای به‌روزرسانی:

`updatectl`

- نمایش داده‌های مقصد و نسخه‌های آن:

`updatectl list {{target}}`

- بازگرداندن داده‌های محلی مقصد بدون دریافت از شبکه:

`updatectl --offline list {{target}}`

- اعمال به‌روزرسانی به مقصد و سپس راه‌اندازی مجدد سیستم:

`updatectl --reboot update {{target}}`

- پاک‌سازی نسخه‌های قدیمی مقصد مشخص:

`updatectl vacuum {{target}}`

- نمایش راهنما:

`updatectl {{[-h|--help]}}`
