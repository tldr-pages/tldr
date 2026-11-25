# btrfs restore

> تلاش برای نجات فایل‌ها از یک سیستم فایل btrfs آسیب‌دیده.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- بازیابی همهٔ فایل‌ها از یک سیستم فایل btrfs به دایرکتوری مشخص:

`sudo btrfs {{[rest|restore]}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- شبیه‌سازی بازیابی و فهرست کردن فایل‌هایی که از یک سیستم فایل btrfs بازیابی خواهند شد:

`sudo btrfs {{[rest|restore]}} {{[-D|--dry-run]}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- بازیابی فایل‌های مطابق با عبارت منظم `regex` بدون حساسیت به بزرگی و کوچکی حروف با `-c` (همهٔ دایرکتوری‌های والد فایل‌های هدف نیز باید با عبارت مطابقت داشته باشند):

`sudo btrfs {{[rest|restore]}} --path-regex {{regex}} -c {{path/to/btrfs_device}} {{path/to/target_directory}}`

- بازیابی فایل‌ها از سیستم فایل btrfs با استفاده از مقدار `bytenr` درخت ریشهٔ مشخص‌شده با `-t` (دستور `btrfs-find-root` را ببینید):

`sudo btrfs {{[rest|restore]}} -t {{bytenr}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- بازیابی فایل‌ها از سیستم فایل btrfs همراه با فراداده، ویژگی‌های گسترش‌یافته و پیوندهای نمادین، با بازنویسی فایل‌های مقصد:

`sudo btrfs {{[rest|restore]}} {{[-m|--metadata]}} {{[-x|--xattr]}} {{[-S|--symlinks]}} {{[-o|--overwrite]}} {{path/to/btrfs_device}} {{path/to/target_directory}}`
