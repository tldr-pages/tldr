# pacman

> واحد مدیریت پکیج آرچ لینوکس
> همچنین : `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> برای دیدن دستور های معادل در سایر پکیج منیجر ها <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> اطلاعات بیشتر: <https://man.archlinux.org/man/pacman.8>.

- همگام سازی و بروز رسانی تمام پکیج ها:

`sudo pacman -Syu`

- نصب پکیج جدید:

`sudo pacman -S {{package}}`

- حذف یک پکیج به همراه وابستگی هاش:

`sudo pacman -Rs {{package}}`

- جستجو در دیتابیس برای پکیج هایی که با یک فایل خاص تعارض دارند:

`pacman -F "{{file_name}}"`

- لیست کردن پکیج های نصب شده با نسخه آنها:

`pacman -Q`

- لیست کردن تنها پکیج هایی که مستقیما نصب شده اند به همراه نسخه آنها:

`pacman -Qe`

- لیست کردن پکیج هایی که به عنوان وابستگی نصب شده اند اما توسط هیچ پکیجی استفاده نمیشوند:

`pacman -Qtdq`

- خالی کردن کل کش  `pacman`:

`sudo pacman -Scc`
