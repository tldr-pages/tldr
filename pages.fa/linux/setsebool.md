# setsebool

> تنظیم مقدار بولی SELinux.
> همچنین ببینید: `semanage boolean`, `getsebool`.
> اطلاعات بیشتر: <https://manned.org/setsebool>.

- نمایش تنظیم فعلی همهٔ مقادیر بولی:

`getsebool -a`

- تنظیم یا لغو موقت مقدار بولی (پس از راه‌اندازی مجدد پایدار نیست):

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- تنظیم یا لغو دائمی مقدار بولی:

`sudo setsebool -P {{container_use_devices}} {{1|true|on|0|false|off}}`

- تنظیم یا لغو دائمی چند مقدار بولی هم‌زمان:

`sudo setsebool -P {{key1 1 key2 0 ...}}`

- تنظیم یا لغو دائمی مقدار بولی (روش جایگزین با `semanage-boolean`):

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
