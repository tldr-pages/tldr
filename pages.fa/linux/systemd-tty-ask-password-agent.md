# systemd-tty-ask-password-agent

> فهرست یا پردازش درخواست‌های رمز عبور systemd در انتظار.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-tty-ask-password-agent.html>.

- فهرست کردن همهٔ درخواست‌های فعلی رمز عبور سیستم در انتظار:

`systemd-tty-ask-password-agent --list`

- پردازش پیوستهٔ درخواست‌های رمز عبور:

`systemd-tty-ask-password-agent --watch`

- پردازش همهٔ درخواست‌های فعلی رمز عبور سیستم در انتظار با پرسش از کاربر در TTY فراخواننده:

`systemd-tty-ask-password-agent --query`

- ارسال درخواست‌های رمز عبور به wall به‌جای پرسش از کاربر در TTY فراخواننده:

`systemd-tty-ask-password-agent --wall`
