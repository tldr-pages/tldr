# userdbctl

> بررسی کاربران، گروه‌ها و عضویت‌های گروه در سیستم.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/userdbctl.html>.

- فهرست کردن همهٔ رکوردهای کاربر شناخته‌شده:

`userdbctl`

- نمایش جزئیات کاربر مشخص:

`userdbctl user {{username}}`

- فهرست کردن همهٔ گروه‌های شناخته‌شده:

`userdbctl group`

- نمایش جزئیات گروه مشخص:

`userdbctl group {{groupname}}`

- فهرست کردن همهٔ سرویس‌هایی که اکنون تعریف کاربر یا گروه را به سیستم ارائه می‌کنند:

`userdbctl services`
