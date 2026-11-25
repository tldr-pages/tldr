# xdg-settings

> مدیریت تنظیمات محیط‌های دسکتاپ سازگار با XDG.
> اطلاعات بیشتر: <https://portland.freedesktop.org/doc/xdg-settings.html>.

- چاپ مرورگر وب پیش‌فرض:

`xdg-settings get default-web-browser`

- تنظیم مرورگر وب پیش‌فرض به Firefox:

`xdg-settings set default-web-browser {{firefox.desktop}}`

- تنظیم مدیریت‌کنندهٔ پیش‌فرض طرح URL ایمیل به Evolution:

`xdg-settings set default-url-scheme-handler mailto {{evolution.desktop}}`

- تنظیم نمایش‌دهندهٔ پیش‌فرض اسناد PDF:

`xdg-settings set {{pdf-viewer.desktop}}`

- نمایش راهنما:

`xdg-settings --help`
