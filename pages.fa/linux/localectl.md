# localectl

> کنترل تنظیمات محلی سیستم و چیدمان صفحه‌کلید.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/localectl.html>.

- نمایش تنظیمات فعلی محیط محلی سیستم و نگاشت صفحه‌کلید:

`localectl`

- فهرست کردن تنظیمات محلی موجود:

`localectl list-locales`

- تنظیم متغیر تنظیمات محلی سیستم:

`localectl set-locale {{LANG}}={{en_US.UTF-8}}`

- فهرست کردن نگاشت‌های کلید موجود:

`localectl list-keymaps`

- تنظیم نگاشت صفحه‌کلید سیستم برای کنسول و نشست‌های گرافیکی:

`localectl set-keymap {{us}}`
