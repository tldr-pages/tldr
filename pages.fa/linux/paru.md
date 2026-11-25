# paru

> ابزار کمکی AUR و واسط pacman.
> همچنین : `pacman`, `yay`.
> اطلاعات بیشتر: <https://github.com/Morganamilo/paru#examples>.

- جست‌وجو و نصب تعاملی بسته:

`paru {{package_name_or_search_term}}`

- همگام‌سازی و به‌روزرسانی همهٔ بسته‌ها:

`paru`

- ارتقای بسته‌های AUR:

`paru -Sua`

- فهرست کردن بسته‌های نصب‌شده به‌صورت دستی:

`paru -Qqm`

- حذف بستهٔ نصب‌شده، فایل‌های پیکربندی و وابستگی‌های آن:

`paru -Rns {{package}}`

- دریافت اطلاعات بسته:

`paru -Si {{package}}`

- بارگیری `PKGBUILD` و سایر فایل‌های منبع بسته از AUR یا ABS:

`paru --getpkgbuild {{package}}`

- نمایش فایل `PKGBUILD` بسته:

`paru -Gp {{package}}`
