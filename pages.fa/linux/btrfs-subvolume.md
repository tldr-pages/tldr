# btrfs subvolume

> مدیریت زیرحجم‌ها و عکس‌های لحظه‌ای btrfs.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- ایجاد یک زیرحجم خالی جدید:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{path/to/new_subvolume}}`

- فهرست کردن همهٔ زیرحجم‌ها و عکس‌های لحظه‌ای در سیستم فایل مشخص‌شده:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{path/to/btrfs_filesystem}}`

- حذف یک زیرحجم:

`sudo btrfs {{[su|subvolume]}} {{[d|delete]}} {{path/to/subvolume}}`

- ایجاد یک عکس لحظه‌ای فقط‌خواندنی از یک زیرحجم موجود با `-r`:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} -r {{path/to/source_subvolume}} {{path/to/target}}`

- ایجاد یک عکس لحظه‌ای خواندنی و نوشتنی از یک زیرحجم موجود:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} {{path/to/source_subvolume}} {{path/to/target}}`

- نمایش اطلاعات مفصل دربارهٔ یک زیرحجم:

`sudo btrfs {{[su|subvolume]}} {{[sh|show]}} {{path/to/subvolume}}`
