# apx subsystems

> مدیریت زیرسیستم‌ها در `apx`.
> زیرسیستم‌ها کانتینرهایی هستند که می‌توان بر اساس پشته‌های موجود ساخت.
> اطلاعات بیشتر: <https://docs.vanillaos.org/docs/en/apx-manpage#subsystems>.

- ساخت تعاملی یک زیرسیستم جدید:

`apx subsystems new`

- فهرست کردن همهٔ زیرسیستم‌های موجود:

`apx subsystems list`

- بازنشانی یک زیرسیستم مشخص به وضعیت اولیه:

`apx subsystems reset {{[-n|--name]}} {{string}}`

- بازنشانی اجباری یک زیرسیستم مشخص:

`apx subsystems reset {{[-n|--name]}} {{string}} {{[-f|--force]}}`

- حذف یک زیرسیستم مشخص:

`apx subsystems rm {{[-n|--name]}} {{string}}`

- حذف اجباری یک زیرسیستم مشخص:

`apx subsystems rm {{[-n|--name]}} {{string}} {{[-f|--force]}}`
