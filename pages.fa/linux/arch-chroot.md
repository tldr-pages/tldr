# arch-chroot

> دستور بهبودیافتهٔ `chroot` برای کمک به فرایند نصب آرچ لینوکس.
> اطلاعات بیشتر: <https://manned.org/arch-chroot>.

- شروع یک پوستهٔ تعاملی (به‌صورت پیش‌فرض Bash) در یک دایرکتوری ریشهٔ جدید:

`arch-chroot {{path/to/new_root}}`

- تعیین کاربری غیر از کاربر فعلی برای اجرای پوسته:

`arch-chroot -u {{user}} {{path/to/new_root}}`

- اجرای یک دستور دلخواه (به جای Bash پیش‌فرض) در دایرکتوری ریشهٔ جدید:

`arch-chroot {{path/to/new_root}} {{command}} {{command_arguments}}`

- تعیین پوسته‌ای غیر از Bash پیش‌فرض (در این مورد بستهٔ `zsh` باید روی سیستم مقصد نصب شده باشد):

`arch-chroot {{path/to/new_root}} {{zsh}}`
