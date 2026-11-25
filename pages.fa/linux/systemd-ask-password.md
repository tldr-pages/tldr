# systemd-ask-password

> درخواست رمز عبور سیستم از کاربر.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-ask-password.html>.

- درخواست رمز عبور سیستم با پیام مشخص:

`systemd-ask-password "{{prompt}}"`

- تعیین شناسه برای درخواست رمز عبور:

`systemd-ask-password --id {{identifier}} "{{prompt}}"`

- استفاده از نام کلید حلقهٔ کلید هسته به‌عنوان حافظهٔ نهان رمز عبور:

`systemd-ask-password --keyname {{key_name}} "{{prompt}}"`

- تنظیم مهلت دلخواه درخواست رمز عبور:

`systemd-ask-password --timeout {{seconds}} "{{prompt}}"`

- اجبار استفاده از سیستم عامل و درخواست نکردن در TTY فعلی:

`systemd-ask-password --no-tty "{{prompt}}"`

- ذخیرهٔ رمز عبور در حلقهٔ کلید هسته بدون نمایش آن:

`systemd-ask-password --no-output --keyname {{key_name}} "{{prompt}}"`

- ارسال رمز عبور به دستور با حذف خط جدید انتهایی:

`systemd-ask-password -n | {{command}}`

- نمایش راهنما:

`systemd-ask-password {{[-h|--help]}}`
