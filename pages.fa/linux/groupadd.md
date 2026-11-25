# groupadd

> افزودن گروه‌های کاربری به سیستم.
> همچنین : `groups`, `groupdel`, `groupmod`.
> اطلاعات بیشتر: <https://manned.org/groupadd>.

- ایجاد یک گروه جدید:

`sudo groupadd {{group_name}}`

- ایجاد یک گروه سیستمی جدید:

`sudo groupadd {{[-r|--system]}} {{group_name}}`

- ایجاد یک گروه جدید با شناسهٔ گروه مشخص:

`sudo groupadd {{[-g|--gid]}} {{group_id}} {{group_name}}`
