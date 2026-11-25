# userdel

> حذف حساب کاربری یا حذف کاربر از گروه.
> همچنین : `users`, `useradd`, `usermod`.
> اطلاعات بیشتر: <https://manned.org/userdel>.

- حذف کاربر:

`sudo userdel {{username}}`

- حذف کاربر در دایرکتوری ریشهٔ دیگر:

`sudo userdel {{[-R|--root]}} {{path/to/other_root}} {{username}}`

- حذف کاربر همراه با دایرکتوری خانگی و صف ایمیل:

`sudo userdel {{[-r|--remove]}} {{username}}`
