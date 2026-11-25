# systemd-cat

> اتصال جریان‌های خروجی خط لوله یا برنامه به گزارش systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-cat.html>.

- نوشتن خروجی دستور مشخص در گزارش (هر دو جریان خروجی ضبط می‌شوند):

`systemd-cat {{command}}`

- نوشتن خروجی خط لوله در گزارش (`stderr` به ترمینال متصل می‌ماند):

`{{command}} | systemd-cat`

- استفاده از شناسهٔ مشخص (پیش‌فرض `cat` هنگام خواندن از خط لوله و در غیر این صورت نام فایل اجرایی):

`{{command}} | systemd-cat {{[-t|--identifier]}} {{id}}`

- استفاده از سطح اولویت پیش‌فرض مشخص برای همهٔ پیام‌های ثبت‌شده:

`systemd-cat {{[-p|--priority]}} {{emerg|alert|crit|err|warning|notice|info|debug}} {{command}}`

- استفاده از سطح اولویت پیش‌فرض مشخص برای پیام‌های ثبت‌شده از `stderr` دستور:

`systemd-cat --stderr-priority {{emerg|alert|crit|err|warning|notice|info|debug}} {{command}}`
