# mkarchiso

> ساخت تصاویر ISO مربوط به Arch Linux از پروفایل archiso.
> اطلاعات بیشتر: <https://manned.org/mkarchiso>.

- ساخت ISO از پروفایل رسمی `releng`:

`mkarchiso -v /usr/share/archiso/configs/releng`

- ساخت ISO با دایرکتوری‌های کاری و خروجی دلخواه:

`mkarchiso -v -w {{path/to/work_directory}} -o {{path/to/output_directory}} {{path/to/profile_directory}}`

- ساخت ISO و حذف دایرکتوری کاری پس از آن:

`mkarchiso -r -o {{path/to/output_directory}} {{path/to/profile_directory}}`

- ساخت tarball راه‌اندازی اولیه و فایل‌های netboot به‌جای ISO:

`mkarchiso -m "{{bootstrap netboot}}" {{path/to/profile_directory}}`

- تنظیم برچسب حجم، ناشر و نام برنامهٔ ISO:

`mkarchiso -L {{label}} -P "{{publisher}}" -A "{{application}}" {{path/to/profile_directory}}`

- نصب بسته‌های اضافی در تصویر:

`mkarchiso -p "{{package1 package2 ...}}" {{path/to/profile_directory}}`

- نمایش راهنما:

`mkarchiso -h`
