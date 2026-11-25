# semanage interface

> مدیریت تعریف‌های نوع واسط شبکهٔ SELinux.
> همچنین : `semanage port`.
> اطلاعات بیشتر: <https://manned.org/semanage-interface>.

- فهرست کردن همهٔ تعریف‌های نوع واسط:

`sudo semanage interface {{[-l|--list]}}`

- افزودن تعریف نوع واسط شبکه:

`sudo semanage interface {{[-a|--add]}} {{[-t|--type]}} {{type_name}} {{interface_name}}`

- حذف تعریف نوع واسط شبکه:

`sudo semanage interface {{[-d|--delete]}} {{interface_name}}`

- تغییر تعریف نوع واسط شبکه:

`sudo semanage interface {{[-m|--modify]}} {{[-t|--type]}} {{type_name}} {{interface_name}}`

- فهرست کردن تعریف‌های نوع واسط در قالب سفارشی:

`sudo semanage interface {{[-l|--list]}} {{[-C|--locallist]}}`
