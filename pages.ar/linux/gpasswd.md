# gpasswd

> إدارة `/etc/group` و `/etc/gshadow`.
> لمزيد من التفاصيل: <https://manned.org/gpasswd>.

- عرّف مديرين المجموعة المسماة:

`sudo gpasswd -A {{user1,user2}} {{group}}`

- عين أعضاء المجموعة المسماة:

`sudo gpasswd -M {{user1,user2}} {{group}}`

- إنشئ رقم سري للمجموعة المسماة:

`gpasswd {{group}}`

- أضف عضو إلي المجموعة المسماة:

`gpasswd -a {{user}} {{group}}`

- إحذف عضو من المجموعة المسماة:

`gpasswd -d {{user}} {{group}}`
