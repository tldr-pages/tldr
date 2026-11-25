# btrfs property

> دریافت، تنظیم یا فهرست کردن ویژگی‌های یک شیء سیستم فایل BTRFS (فایل‌ها، دایرکتوری‌ها، زیرحجم‌ها، سیستم‌های فایل یا دستگاه‌ها).
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-property.html>.

- فهرست کردن ویژگی‌های موجود و توضیحات آن‌ها برای شیء btrfs مشخص:

`sudo btrfs {{[p|property]}} {{[l|list]}} {{path/to/btrfs_object}}`

- دریافت همهٔ ویژگی‌های شیء btrfs مشخص:

`sudo btrfs {{[p|property]}} {{[g|get]}} {{path/to/btrfs_object}}`

- دریافت ویژگی `label` برای سیستم فایل یا دستگاه btrfs مشخص:

`sudo btrfs {{[p|property]}} {{[g|get]}} {{path/to/btrfs_filesystem}} label`

- دریافت همهٔ ویژگی‌های مختص نوع شیء برای سیستم فایل یا دستگاه btrfs مشخص:

`sudo btrfs {{[p|property]}} {{[g|get]}} -t {{subvol|filesystem|inode|device}} {{path/to/btrfs_filesystem}}`

- تنظیم ویژگی `compression` برای یک inode مشخص btrfs (فایل یا دایرکتوری):

`sudo btrfs {{[p|property]}} {{[s|set]}} {{path/to/btrfs_inode}} compression {{zstd|zlib|lzo|none}}`

- تنظیم ویژگی `ro` (فقط‌خواندنی) برای یک زیرحجم مشخص btrfs:

`sudo btrfs {{[p|property]}} {{[s|set]}} {{path/to/btrfs_subvolume}} ro {{true|false}}`
