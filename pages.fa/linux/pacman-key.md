# pacman-key

> اسکریپت واسط GnuPG برای مدیریت حلقهٔ کلید pacman.
> همچنین ببینید: `pacman`.
> اطلاعات بیشتر: <https://manned.org/pacman-key>.

- مقداردهی اولیهٔ حلقهٔ کلید `pacman`:

`sudo pacman-key --init`

- افزودن کلیدهای پیش‌فرض Arch Linux:

`sudo pacman-key --populate`

- فهرست کردن کلیدهای حلقهٔ کلید عمومی:

`pacman-key {{[-l|--list-keys]}}`

- افزودن کلیدهای مشخص:

`sudo pacman-key {{[-a|--add]}} {{path/to/keyfile.gpg}}`

- دریافت کلید از سرور کلید:

`sudo pacman-key {{[-r|--recv-keys]}} "{{uid|name|email}}"`

- چاپ اثر انگشت کلید مشخص:

`pacman-key {{[-f|--finger]}} "{{uid|name|email}}"`

- امضای محلی کلید واردشده:

`sudo pacman-key --lsign-key "{{uid|name|email}}"`

- حذف کلید مشخص:

`sudo pacman-key {{[-d|--delete]}} "{{uid|name|email}}"`
