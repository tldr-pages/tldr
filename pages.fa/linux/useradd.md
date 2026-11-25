# useradd

> ایجاد کاربر جدید.
> همچنین ببینید: `users`, `userdel`, `usermod`.
> اطلاعات بیشتر: <https://manned.org/useradd>.

- ایجاد کاربر جدید:

`sudo useradd {{username}}`

- ایجاد کاربر جدید با شناسهٔ کاربری مشخص:

`sudo useradd {{[-u|--uid]}} {{user_id}} {{username}}`

- ایجاد کاربر جدید با پوستهٔ مشخص:

`sudo useradd {{[-s|--shell]}} {{path/to/shell}} {{username}}`

- ایجاد کاربر جدید عضو گروه‌های اضافی (به نبود فاصله توجه کنید):

`sudo useradd {{[-G|--groups]}} {{group1,group2,...}} {{username}}`

- ایجاد کاربر جدید با دایرکتوری خانگی پیش‌فرض:

`sudo useradd {{[-m|--create-home]}} {{username}}`

- ایجاد کاربر جدید با دایرکتوری خانگی پرشده از فایل‌های دایرکتوری قالب:

`sudo useradd {{[-k|--skel]}} {{path/to/template_directory}} {{[-m|--create-home]}} {{username}}`

- ایجاد کاربر سیستمی جدید بدون دایرکتوری خانگی:

`sudo useradd {{[-r|--system]}} {{username}}`
