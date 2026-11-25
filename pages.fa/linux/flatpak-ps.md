# flatpak ps

> فهرست کردن نمونه‌های در حال اجرای Flatpak.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-ps>.

- فهرست کردن نمونه‌های در حال اجرا:

`flatpak ps`

- نمایش شناسهٔ برنامه و شناسهٔ فرایند محیط ایزوله برای هر نمونه:

`flatpak ps --columns application,child-pid`

- نمایش محیط اجرا و شاخهٔ آن در کنار هر شناسهٔ برنامه:

`flatpak ps --columns application,runtime,runtime-branch`

- فهرست کردن ستون‌های موجود:

`flatpak ps --columns help`
