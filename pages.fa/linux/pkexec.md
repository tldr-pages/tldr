# pkexec

> اجرای دستورها با هویت کاربر دیگر.
> در صورت وجود رابط گرافیکی، رمز عبور را در آن درخواست می‌کند.
> همچنین ببینید: `sudo`, `run0`, `doas`.
> اطلاعات بیشتر: <https://polkit.pages.freedesktop.org/polkit/pkexec.1.html>.

- اجرای دستور با دسترسی root:

`pkexec {{command}}`

- تغییر کاربر به root:

`pkexec`

- اجرای دستور با کاربر مشخص:

`pkexec --user {{username}} {{command}}`
