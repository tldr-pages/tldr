# semanage login

> مدیریت نگاشت‌های ورود SELinux بین کاربران لینوکس و کاربران SELinux.
> همچنین ببینید: `semanage user`.
> اطلاعات بیشتر: <https://manned.org/semanage-login>.

- فهرست کردن همهٔ نگاشت‌های ورود:

`sudo semanage login {{[-l|--list]}}`

- افزودن نگاشت ورود (نگاشت کاربر لینوکس به کاربر SELinux):

`sudo semanage login {{[-a|--add]}} {{[-s|--seuser]}} {{selinux_user}} {{linux_username}}`

- حذف نگاشت ورود:

`sudo semanage login {{[-d|--delete]}} {{linux_username}}`

- تغییر نگاشت ورود موجود:

`sudo semanage login {{[-m|--modify]}} {{[-s|--seuser]}} {{selinux_user}} {{linux_username}}`

- افزودن نگاشت ورود با بازهٔ MLS/MCS مشخص:

`sudo semanage login {{[-a|--add]}} {{[-s|--seuser]}} {{user_u}} {{[-r|--range]}} {{s0-s0:c0.c1023}} {{linux_username}}`

- فهرست کردن فقط نگاشت‌های ورود سفارشی:

`sudo semanage login {{[-l|--list]}} {{[-C|--locallist]}}`
