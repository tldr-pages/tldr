# semodule

> مدیریت ماژول‌های سیاست SELinux.
> همچنین ببینید: `audit2allow`, `semanage`.
> اطلاعات بیشتر: <https://manned.org/semodule>.

- فهرست کردن همهٔ ماژول‌های سیاست نصب‌شده:

`sudo semodule {{[-l|--list]}}`

- نصب ماژول سیاست جدید:

`sudo semodule {{[-i|--install]}} {{path/to/module.pp}}`

- حذف ماژول سیاست:

`sudo semodule {{[-r|--remove]}} {{module_name}}`

- فعال کردن ماژول سیاست:

`sudo semodule {{[-e|--enable]}} {{module_name}}`

- غیرفعال کردن ماژول سیاست:

`sudo semodule {{[-d|--disable]}} {{module_name}}`

- بارگذاری مجدد همهٔ ماژول‌های سیاست:

`sudo semodule {{[-R|--reload]}}`

- نمایش نسخهٔ ماژول‌های سیاست نصب‌شده:

`sudo semodule {{[-l|--list]}} {{[-v|--verbose]}}`
