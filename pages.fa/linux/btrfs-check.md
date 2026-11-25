# btrfs check

> بررسی یا تعمیر یک سیستم فایل btrfs.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-check.html>.

- بررسی یک سیستم فایل btrfs:

`sudo btrfs {{[c|check]}} {{path/to/partition}}`

- بررسی و تعمیر یک سیستم فایل btrfs (خطرناک):

`sudo btrfs {{[c|check]}} --repair {{path/to/partition}}`

- نمایش پیشرفت بررسی:

`sudo btrfs {{[c|check]}} {{[-p|--progress]}} {{path/to/partition}}`

- بررسی مجموع مقابله‌ای هر بلوک داده (اگر سیستم فایل سالم باشد):

`sudo btrfs {{[c|check]}} --check-data-csum {{path/to/partition}}`

- استفاده از ابر‌بلوک شمارهٔ `n` (مقدار `n` می‌تواند 0، 1 یا 2 باشد):

`sudo btrfs {{[c|check]}} {{[-s|--super]}} {{n}} {{path/to/partition}}`

- بازسازی درخت مجموع مقابله‌ای:

`sudo btrfs {{[c|check]}} --repair --init-csum-tree {{path/to/partition}}`

- بازسازی درخت extent:

`sudo btrfs {{[c|check]}} --repair --init-extent-tree {{path/to/partition}}`
