# semanage user

> مدیریت نگاشت‌های کاربر SELinux.
> همچنین ببینید: `semanage login`.
> اطلاعات بیشتر: <https://manned.org/semanage-user>.

- فهرست کردن همهٔ کاربران SELinux:

`sudo semanage user {{[-l|--list]}}`

- افزودن کاربر جدید SELinux:

`sudo semanage user {{[-a|--add]}} {{[-R|--roles]}} {{role_name}} {{selinux_user}}`

- حذف کاربر SELinux:

`sudo semanage user {{[-d|--delete]}} {{selinux_user}}`

- تغییر نقش‌های کاربر موجود SELinux:

`sudo semanage user {{[-m|--modify]}} {{[-R|--roles]}} {{role_name}} {{selinux_user}}`

- افزودن کاربر SELinux با سطح پیش‌فرض مشخص:

`sudo semanage user {{[-a|--add]}} {{[-R|--roles]}} {{role_name}} {{[-L|--level]}} {{s0}} {{selinux_user}}`

- افزودن کاربر SELinux با بازهٔ MLS/MCS مشخص:

`sudo semanage user {{[-a|--add]}} {{[-R|--roles]}} {{role_name}} {{[-r|--range]}} {{s0-s0:c0.c1023}} {{selinux_user}}`

- فهرست کردن فقط کاربران سفارشی SELinux:

`sudo semanage user {{[-l|--list]}} {{[-C|--locallist]}}`
