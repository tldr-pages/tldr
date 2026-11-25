# btrfs scrub

> بررسی سیستم‌های فایل btrfs با عملیات scrub برای تأیید یکپارچگی داده‌ها.
> توصیه می‌شود هر ماه یک بار عملیات scrub اجرا شود.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- شروع عملیات scrub:

`sudo btrfs {{[sc|scrub]}} start {{path/to/btrfs_mount}}`

- نمایش وضعیت عملیات scrub در حال اجرا یا آخرین عملیات کامل‌شده:

`sudo btrfs {{[sc|scrub]}} status {{path/to/btrfs_mount}}`

- لغو عملیات scrub در حال اجرا:

`sudo btrfs {{[sc|scrub]}} {{[c|cancel]}} {{path/to/btrfs_mount}}`

- از سر گرفتن عملیات scrub که پیش‌تر لغو شده است:

`sudo btrfs {{[sc|scrub]}} {{[r|resume]}} {{path/to/btrfs_mount}}`

- شروع عملیات scrub بدون فرستادن برنامه به پس‌زمینه با `-B`:

`sudo btrfs {{[sc|scrub]}} start -B {{path/to/btrfs_mount}}`

- شروع عملیات scrub در حالت بی‌صدا (خطاها یا آمار را چاپ نمی‌کند):

`sudo btrfs {{[sc|scrub]}} start {{[-q|--quiet]}} {{path/to/btrfs_mount}}`
