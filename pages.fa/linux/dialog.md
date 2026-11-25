# dialog

> نمایش جعبه‌های گفت‌وگو در پایانه.
> همچنین : `gum`, `whiptail`.
> اطلاعات بیشتر: <https://manned.org/dialog>.

- نمایش یک پیام:

`dialog --msgbox "{{Message}}" {{height}} {{width}}`

- درخواست متن از کاربر:

`dialog --inputbox "{{Enter text:}}" {{8}} {{40}} 2>{{output.txt}}`

- پرسیدن یک سؤال بله یا خیر از کاربر:

`dialog --yesno "{{Continue?}}" {{7}} {{40}}`

- نمایش راهنما:

`dialog`
