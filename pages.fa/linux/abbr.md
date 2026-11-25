# abbr

> مدیریت مخفف‌ها برای پوستهٔ fish.
> واژه‌های تعریف‌شده توسط کاربر پس از ورود با عبارت‌های طولانی‌تر جایگزین می‌شوند.
> اطلاعات بیشتر: <https://fishshell.com/docs/current/cmds/abbr.html>.

- افزودن یک مخفف جدید:

`abbr {{[-a|--add]}} {{abbreviation_name}} {{command}} {{command_arguments}}`

- تغییر نام یک مخفف موجود:

`abbr --rename {{old_name}} {{new_name}}`

- حذف یک مخفف موجود:

`abbr {{[-e|--erase]}} {{abbreviation_name}}`

- وارد کردن مخفف‌های تعریف‌شده در یک میزبان دیگر از طریق SSH:

`ssh {{host_name}} abbr {{[-s|--show]}} | source`
