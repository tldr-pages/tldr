# rpm

> مدیر بستهٔ RPM.
> برای دستورهای معادل در سایر مدیران بسته، <https://wiki.archlinux.org/title/Pacman/Rosetta> را ببینید.
> اطلاعات بیشتر: <https://rpm-software-management.github.io/rpm/man/rpm.8>.

- نمایش نسخهٔ بستهٔ httpd:

`rpm {{[-q|--query]}} httpd`

- فهرست کردن نسخه‌های همهٔ بسته‌های مطابق:

`rpm {{[-qa|--query --all]}} '{{mariadb*}}'`

- نصب اجباری بسته بدون توجه به نسخه‌های نصب‌شدهٔ فعلی:

`rpm {{[-U|--upgrade]}} {{path/to/package.rpm}} --force`

- شناسایی مالک فایل و نمایش نسخهٔ بسته:

`rpm {{[-qf|--query --file]}} {{/etc/postfix/main.cf}}`

- فهرست کردن فایل‌های متعلق به بسته:

`rpm {{[-ql|--query --list]}} {{kernel}}`

- نمایش scriptletها از فایل RPM:

`rpm {{[-qp|--query --package]}} --scripts {{package.rpm}}`

- نمایش فایل‌های تغییرکرده، گمشده یا نادرست نصب‌شدهٔ بسته‌های مطابق:

`rpm {{[-Va|--verify --all]}} '{{php-*}}'`

- نمایش تغییرنامهٔ بستهٔ مشخص:

`rpm {{[-q|--query]}} --changelog {{package}}`
