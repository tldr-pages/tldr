# abbr

> fish shell مدیریت مخفف های
> جایگزین کردن کلمات وارد شده توسط کاربر با جملات طولانی
> اطلاعات بیشتر: <https://fishshell.com/docs/current/cmds/abbr.html>.

- اضافه کردن مخفف جدید:

`abbr --add {{abbreviation_name}} {{command}} {{command_arguments}}`

- تغییر نام یک مخفف موجود:

`abbr --rename {{old_name}} {{new_name}}`

- پاک کردن یک مخفف موجود:

`abbr --erase {{abbreviation_name}}`

- وارد کردن یک مخفف وارد شده در یک میزبان دیگر از طریق ssh:

`ssh {{host_name}} abbr --show | source`
