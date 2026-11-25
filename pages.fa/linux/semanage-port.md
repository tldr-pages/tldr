# semanage port

> مدیریت تعریف‌های پایدار پورت SELinux.
> اطلاعات بیشتر: <https://manned.org/semanage-port>.

- فهرست کردن همهٔ قوانین برچسب‌گذاری پورت:

`sudo semanage port {{[-l|--list]}}`

- فهرست کردن همهٔ قوانین برچسب‌گذاری پورت تعریف‌شده توسط کاربر بدون سربرگ:

`sudo semanage port {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- افزودن قانون کاربری که برچسبی به جفت پروتکل و پورت اختصاص می‌دهد:

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{ssh_port_t}} {{[-p|--proto]}} {{tcp}} {{22000}}`

- افزودن قانون کاربری که برچسبی به جفت پروتکل و بازهٔ پورت اختصاص می‌دهد:

`sudo semanage port {{[-a|--add]}} {{[-t|--type]}} {{http_port_t}} {{[-p|--proto]}} {{tcp}} {{80-88}}`

- حذف قانون کاربری با جفت پروتکل و پورت آن:

`sudo semanage port {{[-d|--delete]}} {{[-p|--proto]}} {{udp}} {{11940}}`
