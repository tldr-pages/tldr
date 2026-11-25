# systemctl switch-root

> تغییر به فایل‌سیستم ریشهٔ جدید و اجرای مدیر سیستم جدید.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#switch-root%20ROOT%20INIT>.

- تغییر به فایل‌سیستم ریشهٔ جدید و اجرای سیستم init پیش‌فرض آن:

`systemctl switch-root {{path/to/new_root}}`

- تغییر به فایل‌سیستم ریشهٔ جدید و اجرای فایل دودویی init مشخص:

`systemctl switch-root {{path/to/new_root}} {{/sbin/init}}`

- تغییر به فایل‌سیستم ریشهٔ جدید با خروجی مفصل:

`systemctl switch-root {{path/to/new_root}} {{[-v|--verbose]}}`
