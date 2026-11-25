# schroot

> اجرای دستور یا شروع پوستهٔ تعاملی با دایرکتوری ریشهٔ متفاوت. قابل سفارشی‌سازی‌تر از `chroot`.
> اطلاعات بیشتر: <https://wiki.debian.org/Schroot>.

- فهرست کردن chrootهای موجود:

`schroot --list`

- اجرای دستور در chroot مشخص:

`schroot --chroot {{chroot}} {{command}}`

- اجرای دستور با گزینه‌ها در chroot مشخص:

`schroot --chroot {{chroot}} {{command}} -- {{command_options}}`

- اجرای دستور در همهٔ chrootهای موجود:

`schroot --all {{command}}`

- شروع پوستهٔ تعاملی در chroot مشخص به‌عنوان کاربر مشخص:

`schroot --chroot {{chroot}} --user {{user}}`

- شروع نشست جدید (شناسهٔ یکتای نشست در `stdout` برگردانده می‌شود):

`schroot --begin-session --chroot {{chroot}}`

- اتصال به نشست موجود:

`schroot --run-session --chroot {{session_id}}`

- پایان نشست موجود:

`schroot --end-session --chroot {{session_id}}`
