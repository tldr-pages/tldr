# btrfs balance

> متعادل‌سازی گروه‌های بلوک در یک سیستم فایل btrfs.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-balance.html>.

- نمایش وضعیت عملیات متعادل‌سازی در حال اجرا یا متوقف‌شده:

`sudo btrfs {{[b|balance]}} status {{path/to/btrfs_filesystem}}`

- متعادل‌سازی همهٔ گروه‌های بلوک (کند است؛ همهٔ بلوک‌های سیستم فایل را بازنویسی می‌کند):

`sudo btrfs {{[b|balance]}} start {{path/to/btrfs_filesystem}}`

- متعادل‌سازی گروه‌های بلوک داده با کمتر از ۱۵ درصد استفاده و اجرای عملیات در پس‌زمینه:

`sudo btrfs {{[b|balance]}} start {{[--bg|--background]}} -dusage=15 {{path/to/btrfs_filesystem}}`

- متعادل‌سازی حداکثر ۱۰ قطعهٔ فراداده با کمتر از ۲۰ درصد استفاده و حداقل ۱ قطعه روی دستگاه مشخص با شناسهٔ `devid` (دستور `btrfs filesystem show` را ببینید):

`sudo btrfs {{[b|balance]}} start -musage=20,limit=10,devid=devid {{path/to/btrfs_filesystem}}`

- تبدیل بلوک‌های داده به raid6 و فراداده به raid1c3 (برای پروفایل‌ها mkfs.btrfs(8) را ببینید):

`sudo btrfs {{[b|balance]}} start -dconvert=raid6 -mconvert=raid1c3 {{path/to/btrfs_filesystem}}`

- تبدیل بلوک‌های داده به raid1 با صرف‌نظر از قطعه‌های تبدیل‌شده (برای مثال پس از یک عملیات تبدیل لغوشده):

`sudo btrfs {{[b|balance]}} start -dconvert=raid1,soft {{path/to/btrfs_filesystem}}`

- لغو، توقف موقت یا از سرگیری عملیات متعادل‌سازی در حال اجرا یا متوقف‌شده:

`sudo btrfs {{[b|balance]}} {{cancel|pause|resume}} {{path/to/btrfs_filesystem}}`
