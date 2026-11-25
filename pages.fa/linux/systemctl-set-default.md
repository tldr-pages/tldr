# systemctl set-default

> ایجاد پیوند نمادین نام مستعار `default.target` به واحد هدف مشخص.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-default%20TARGET>.

- تنظیم حالت راه‌اندازی پیش‌فرض `systemd`:

`systemctl set-default {{target_name.target}}`

- تنظیم `systemd` برای راه‌اندازی پیش‌فرض در حالت رابط گرافیکی:

`systemctl set-default graphical.target`

- تنظیم `systemd` برای راه‌اندازی پیش‌فرض در حالت خط فرمان:

`systemctl set-default multi-user.target`
