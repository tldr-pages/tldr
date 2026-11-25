# kpackagetool5

> مدیر KPackage: نصب، فهرست و حذف بسته‌های Plasma.
> اطلاعات بیشتر: <https://manned.org/kpackagetool5>.

- فهرست کردن همهٔ انواع شناخته‌شدهٔ بسته‌های قابل نصب:

`kpackagetool5 --list-types`

- نصب بسته از دایرکتوری:

`kpackagetool5 {{[-t|--type]}} {{package_type}} {{[-i|--install]}} {{path/to/directory}}`

- به‌روزرسانی بستهٔ نصب‌شده از دایرکتوری:

`kpackagetool5 {{[-t|--type]}} {{package_type}} {{[-u|--upgrade]}} {{path/to/directory}}`

- فهرست کردن پلاسمویدهای نصب‌شده (`--global` برای همهٔ کاربران):

`kpackagetool5 {{[-t|--type]}} Plasma/Applet {{[-l|--list]}} {{[-g|--global]}}`

- حذف پلاسموید با نام:

`kpackagetool5 {{[-t|--type]}} Plasma/Applet {{[-r|--remove]}} "{{name}}"`
