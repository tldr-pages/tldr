# cryptsetup luksFormat

> مقداردهی اولیهٔ یک پارتیشن LUKS و نخستین جایگاه کلید آن (۰) با عبارت عبور یا فایل کلید.
> توجه: این عملیات همهٔ داده‌های پارتیشن را بازنویسی می‌کند.
> اطلاعات بیشتر: <https://manned.org/cryptsetup-luksFormat>.

- مقداردهی اولیهٔ یک حجم LUKS با عبارت عبور:

`cryptsetup luksFormat {{/dev/sdXY}}`

- مقداردهی اولیهٔ یک حجم LUKS با فایل کلید:

`cryptsetup luksFormat {{/dev/sdXY}} {{path/to/keyfile}}`

- مقداردهی اولیهٔ یک حجم LUKS با عبارت عبور و تنظیم برچسب آن:

`cryptsetup luksFormat --label {{label}} {{/dev/sdXY}}`
