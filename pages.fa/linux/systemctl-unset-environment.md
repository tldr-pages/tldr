# systemctl unset-environment

> لغو تنظیم یک یا چند متغیر محیطی مدیر سرویس.
> این کار اثر `systemctl set-environment` را برمی‌گرداند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#unset-environment%20VARIABLE%E2%80%A6>.

- لغو تنظیم یک متغیر محیطی:

`systemctl unset-environment {{var}}`

- لغو تنظیم چند متغیر محیطی هم‌زمان:

`systemctl unset-environment {{var1 var2 ...}}`

- لغو تنظیم متغیر محیطی در مدیر سرویس کاربر:

`systemctl unset-environment {{var}} --user`
