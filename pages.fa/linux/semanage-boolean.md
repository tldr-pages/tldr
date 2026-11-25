# semanage boolean

> مدیریت تنظیمات بولی پایدار SELinux.
> همچنین : `getsebool`, `setsebool`.
> اطلاعات بیشتر: <https://manned.org/semanage-boolean>.

- فهرست کردن همهٔ تنظیمات بولی:

`sudo semanage boolean {{[-l|--list]}}`

- فهرست کردن همهٔ تنظیمات بولی تعریف‌شده توسط کاربر بدون سربرگ:

`sudo semanage boolean {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- تنظیم یا لغو دائمی مقدار بولی:

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
