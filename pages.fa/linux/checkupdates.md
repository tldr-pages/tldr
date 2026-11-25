# checkupdates

> بررسی به‌روزرسانی‌های در انتظار در آرچ لینوکس.
> اطلاعات بیشتر: <https://manned.org/checkupdates>.

- همگام‌سازی پایگاه داده و فهرست کردن به‌روزرسانی‌های در انتظار:

`checkupdates`

- فهرست کردن به‌روزرسانی‌های در انتظار بدون همگام‌سازی پایگاه داده:

`checkupdates {{[-n|--nosync]}}`

- نمایش فهرست به‌روزرسانی‌های در انتظار در صورت تفاوت با آخرین استفاده از این گزینه:

`checkupdates {{[-c|--change]}}`

- فهرست کردن به‌روزرسانی‌های در انتظار و دانلود بسته‌ها در حافظهٔ نهان `pacman` (`/var/cache/pacman/pkg`):

`checkupdates {{[-d|--download]}}`

- فهرست کردن به‌روزرسانی‌های در انتظار با استفاده از یک پایگاه دادهٔ مشخص `pacman`:

`CHECKUPDATES_DB={{path/to/directory}} checkupdates`

- نمایش راهنما:

`checkupdates {{[-h|--help]}}`
