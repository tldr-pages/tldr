# dialog

> عرض نافذة حوار في الطرفية (Terminal).
> لمزيد من التفاصيل: <https://manned.org/dialog>.

- عرض رسالة:

`dialog --msgbox "{{Message}}" {{height}} {{width}}`

- مطالبة المستخدم بإدخال نص:

`dialog --inputbox "{{Enter text:}}" {{8}} {{40}} 2>{{output.txt}}`

- مطالبة المستخدم بسؤال بنعم/لا:

`dialog --yesno "{{Continue?}}" {{7}} {{40}}`
