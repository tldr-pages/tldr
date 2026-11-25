# kpackagetool6

> مدیر KPackage: نصب، فهرست و حذف بسته‌های Plasma.
> اطلاعات بیشتر: <https://manned.org/kpackagetool6>.

- فهرست کردن همهٔ انواع شناخته‌شدهٔ بسته‌های قابل نصب:

`kpackagetool6 --list-types`

- نصب بسته از دایرکتوری:

`kpackagetool6 {{[-t|--type]}} {{package_type}} {{[-i|--install]}} {{path/to/directory}}`

- به‌روزرسانی بستهٔ نصب‌شده از دایرکتوری:

`kpackagetool6 {{[-t|--type]}} {{package_type}} {{[-u|--upgrade]}} {{path/to/directory}}`

- فهرست کردن پلاسمویدهای نصب‌شده (`--global` برای همهٔ کاربران):

`kpackagetool6 {{[-t|--type]}} Plasma/Applet {{[-l|--list]}} {{[-g|--global]}}`

- حذف پلاسموید با نام:

`kpackagetool6 {{[-t|--type]}} Plasma/Applet {{[-r|--remove]}} "{{name}}"`
