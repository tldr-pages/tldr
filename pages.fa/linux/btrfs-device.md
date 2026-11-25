# btrfs device

> مدیریت دستگاه‌ها در یک سیستم فایل btrfs.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- افزودن یک یا چند دستگاه به سیستم فایل btrfs:

`sudo btrfs {{[d|device]}} {{[a|add]}} {{path/to/block_device1 path/to/block_device2 ...}} {{path/to/btrfs_filesystem}}`

- حذف یک دستگاه از سیستم فایل btrfs:

`sudo btrfs {{[d|device]}} {{[rem|remove]}} {{path/to/device1|device_id1 path/to/device2|device_id2 ...}}`

- نمایش آمار خطا:

`sudo btrfs {{[d|device]}} {{[st|stats]}} {{path/to/btrfs_filesystem}}`

- پویش همهٔ دیسک‌ها و اطلاع دادن به هسته دربارهٔ همهٔ سیستم‌های فایل btrfs شناسایی‌شده:

`sudo btrfs {{[d|device]}} {{[sc|scan]}} {{[-d|--all-devices]}}`

- نمایش آمار مفصل تخصیص برای هر دیسک:

`sudo btrfs {{[d|device]}} {{[u|usage]}} {{path/to/btrfs_filesystem}}`
