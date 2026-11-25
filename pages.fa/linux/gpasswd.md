# gpasswd

> مدیریت `/etc/group` و `/etc/gshadow`.
> اطلاعات بیشتر: <https://manned.org/gpasswd>.

- تعیین مدیران گروه:

`sudo gpasswd {{[-A|--administrators]}} {{user1,user2}} {{group}}`

- تنظیم فهرست اعضای گروه:

`sudo gpasswd {{[-M|--members]}} {{user1,user2}} {{group}}`

- ایجاد رمز عبور برای گروه مشخص:

`gpasswd {{group}}`

- افزودن کاربر به گروه مشخص:

`gpasswd {{[-a|--add]}} {{user}} {{group}}`

- حذف کاربر از گروه مشخص:

`gpasswd {{[-d|--delete]}} {{user}} {{group}}`
