# gpasswd

> إدارة `/etc/group` و `/etc/gshadow`.
> لمزيد من التفاصيل: <https://manned.org/gpasswd>.

- عرّف مديرين المجموعة المسماة:

`sudo gpasswd {{[-A|--administrators]}} {{user1,user2}} {{group}}`

- عين أعضاء المجموعة المسماة:

`sudo gpasswd {{[-M|--members]}} {{user1,user2}} {{group}}`

- إنشئ رقم سري للمجموعة المسماة:

`gpasswd {{group}}`

- أضف عضو إلي المجموعة المسماة:

`gpasswd {{[-a|--add]}} {{user}} {{group}}`

- إحذف عضو من المجموعة المسماة:

`gpasswd {{[-d|--delete]}} {{user}} {{group}}`
