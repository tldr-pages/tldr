# steamos-bootdebug

> مدیریت فرایند راه‌اندازی SteamOS.
> اطلاعات بیشتر: <https://gitlab.com/users/evlaV/projects>.

- تغییر آنچه SteamOS هنگام راه‌اندازی نمایش می‌دهد:

`sudo steamos-bootdebug {{kernel-debug|kernel-quiet|menu|verbose|quiet|status}}`

- نمایش گزارش هسته فقط در راه‌اندازی بعدی:

`sudo steamos-bootdebug {{kernel-debug-once}}`

- تنظیم ثبت گزارش فرایند راه‌اندازی در فایل:

`sudo steamos-bootdebug log {{enable|disable}}`

- نمایش فایل گزارش ثبت‌شده:

`sudo steamos-bootdebug log show`
