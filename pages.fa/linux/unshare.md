# unshare

> اجرای دستور در فضاهای نام جدید تعریف‌شده توسط کاربر.
> اطلاعات بیشتر: <https://manned.org/unshare>.

- اجرای پوستهٔ پیش‌فرض:

`unshare`

- اجرای دستور بدون اشتراک دسترسی به شبکه‌های متصل:

`sudo unshare {{[-n|--net]}} {{command}} {{argument1 argument2 ...}}`

- اجرای دستور به‌عنوان فرایند فرزند بدون اشتراک اتصال‌ها، فرایندها یا شبکه‌ها:

`sudo unshare {{[-mpnf|--mount --pid --net --fork]}} {{command}} {{argument1 argument2 ...}}`

- ایجاد دستی کانتینر:

`sudo unshare {{[-puinmf|--pid --uts --ipc --net --mount --fork]}} chroot {{path/to/new_root}} {{/bin/sh}}`
