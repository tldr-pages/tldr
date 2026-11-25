# pacman

> ابزار مدیریت بستهٔ Arch Linux.
> برای دستورهای معادل در سایر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> همچنین : `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> اطلاعات بیشتر: <https://manned.org/pacman.8>.

- همگام‌سازی و به‌روزرسانی همهٔ بسته‌ها:

`sudo pacman -Syu`

- نصب بستهٔ جدید:

`sudo pacman -S {{package}}`

- حذف بسته و وابستگی‌های آن:

`sudo pacman -Rs {{package}}`

- جست‌وجوی `regex` یا کلیدواژه در پایگاه دادهٔ بسته‌ها:

`pacman -Ss "{{search_pattern}}"`

- جست‌وجو در پایگاه داده برای بسته‌های حاوی فایل مشخص:

`pacman -F "{{file_name}}"`

- فهرست کردن فقط بسته‌هایی که صریحاً نصب شده‌اند همراه با نسخهٔ آن‌ها:

`pacman -Qe`

- فهرست کردن بسته‌های یتیم (نصب‌شده به‌عنوان وابستگی اما مورد نیاز هیچ بسته‌ای نیستند):

`pacman -Qtdq`

- خالی کردن کل حافظهٔ نهان `pacman`:

`sudo pacman -Scc`
