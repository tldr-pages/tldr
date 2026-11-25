# systemctl set-environment

> تنظیم یک یا چند متغیر محیطی مدیر سرویس.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#set-environment%20VARIABLE=VALUE%E2%80%A6>.

- تنظیم یک متغیر محیطی:

`systemctl set-environment {{variable}} {{value}}`

- تنظیم چند متغیر محیطی هم‌زمان:

`systemctl set-environment {{variable1 value1 variable2 value2 ...}}`

- تنظیم متغیر محیطی برای مدیر سرویس کاربر:

`systemctl set-environment {{variable}} {{value}} --user`
