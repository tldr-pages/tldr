# dnf group

> مدیریت مجموعه‌های مجازی بسته‌ها در سیستم‌های مبتنی بر فدورا.
> اطلاعات بیشتر: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- فهرست کردن گروه‌های DNF با نمایش وضعیت نصب‌شده یا نصب‌نشده در جدول:

`dnf {{[grp|group]}} list`

- نمایش اطلاعات گروه DNF، شامل مخزن و بسته‌های اختیاری:

`dnf {{[grp|group]}} info {{group_name}}`

- نصب گروه DNF:

`dnf {{[grp|group]}} install {{group_name}}`

- حذف گروه DNF:

`dnf {{[grp|group]}} remove {{group_name}}`

- ارتقای گروه DNF:

`dnf {{[grp|group]}} upgrade {{group_name}}`
