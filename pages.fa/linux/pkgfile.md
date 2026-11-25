# pkgfile

> جست‌وجوی فایل‌های بسته‌های مخازن رسمی در سیستم‌های مبتنی بر Arch.
> همچنین ببینید: `pacman files`.
> اطلاعات بیشتر: <https://manned.org/pkgfile>.

- همگام‌سازی پایگاه دادهٔ pkgfile:

`sudo pkgfile --update`

- جست‌وجوی بستهٔ مالک فایل مشخص:

`pkgfile {{filename}}`

- فهرست کردن همهٔ فایل‌های ارائه‌شده توسط بسته:

`pkgfile --list {{package}}`

- فهرست کردن فایل‌های اجرایی ارائه‌شده توسط بسته:

`pkgfile --list --binaries {{package}}`

- جست‌وجوی بستهٔ مالک فایل مشخص بدون حساسیت به بزرگی و کوچکی حروف:

`pkgfile --ignorecase {{filename}}`

- جست‌وجوی بستهٔ مالک فایل مشخص در دایرکتوری `bin` یا `sbin`:

`pkgfile --binaries {{filename}}`

- جست‌وجوی بستهٔ مالک فایل مشخص همراه با نمایش نسخهٔ بسته:

`pkgfile --verbose {{filename}}`

- جست‌وجوی بستهٔ مالک فایل مشخص در مخزن مشخص:

`pkgfile --repo {{repository_name}} {{filename}}`
