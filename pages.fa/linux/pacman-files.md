# pacman --files

> پرس‌وجوی پایگاه دادهٔ محلی فایل‌ها.
> همچنین : `pkgfile`.
> اطلاعات بیشتر: <https://manned.org/pacman.8>.

- به‌روزرسانی پایگاه دادهٔ بسته‌ها:

`sudo pacman -Fy`

- یافتن بستهٔ مالک فایل مشخص:

`pacman -F {{filename}}`

- یافتن بستهٔ مالک فایل مشخص با استفاده از `regex`:

`pacman -Fx '{{regex}}'`

- فهرست کردن فقط نام بسته‌ها:

`pacman -Fq {{filename}}`

- فهرست کردن فایل‌های متعلق به بستهٔ مشخص:

`pacman -Fl {{package}}`

- نمایش راهنما:

`pacman -Fh`
