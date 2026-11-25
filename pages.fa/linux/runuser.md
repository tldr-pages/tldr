# runuser

> اجرای دستورها به‌عنوان کاربر و گروه بدون درخواست رمز عبور.
> اطلاعات بیشتر: <https://manned.org/runuser>.

- اجرای دستور به‌عنوان کاربر دیگر:

`sudo runuser {{user}} {{[-c|--command]}} '{{command}}'`

- اجرای دستور به‌عنوان کاربر و گروه دیگر:

`sudo runuser {{user}} {{[-g|--group]}} {{group}} {{[-c|--command]}} '{{command}}'`

- شروع پوستهٔ ورود به‌عنوان کاربر مشخص:

`sudo runuser {{user}} {{[-l|--login]}}`

- تعیین پوستهٔ اجرا به‌جای پوستهٔ پیش‌فرض (برای ورود نیز کار می‌کند):

`sudo runuser {{user}} {{[-s|--shell]}} {{/bin/sh}}`

- حفظ کل محیط root (فقط در صورت مشخص نبودن `--login`):

`sudo runuser {{user}} {{[-p|--preserve-environment]}} {{[-c|--command]}} '{{command}}'`
