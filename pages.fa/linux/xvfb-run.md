# xvfb-run

> اجرای دستور در محیط سرور مجازی X.
> اطلاعات بیشتر: <https://manned.org/xvfb-run>.

- اجرای دستور مشخص در سرور مجازی X:

`xvfb-run {{command}}`

- تلاش برای یافتن شمارهٔ آزاد سرور اگر پیش‌فرض (۹۹) در دسترس نباشد:

`xvfb-run {{[-a|--auto-servernum]}} {{command}}`

- ارسال آرگومان‌ها به سرور Xvfb:

`xvfb-run {{[-s|--server-args]}} "{{-screen 0 1024x768x24}}" {{command}}`
