# btrfs inspect-internal

> پرس‌وجوی اطلاعات داخلی یک سیستم فایل btrfs.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-inspect-internal.html>.

- چاپ اطلاعات ابر‌بلوک:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{path/to/partition}}`

- چاپ اطلاعات ابر‌بلوک و همهٔ نسخه‌های آن:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-s|dump-super]}} {{[-a|--all]}} {{path/to/partition}}`

- چاپ اطلاعات فرادادهٔ سیستم فایل:

`sudo btrfs {{[i|inspect-internal]}} {{[dump-t|dump-tree]}} {{path/to/partition}}`

- چاپ فهرست فایل‌های inode شمارهٔ `n`:

`sudo btrfs {{[i|inspect-internal]}} {{[i|inode-resolve]}} {{n}} {{path/to/btrfs_mount}}`

- چاپ فهرست فایل‌ها در یک آدرس منطقی مشخص:

`sudo btrfs {{[i|inspect-internal]}} {{[lo|logical-resolve]}} {{logical_address}} {{path/to/btrfs_mount}}`

- چاپ آمار درخت‌های root، extent، csum و fs:

`sudo btrfs {{[i|inspect-internal]}} {{[t|tree-stats]}} {{path/to/partition}}`
