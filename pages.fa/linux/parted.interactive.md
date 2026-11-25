# parted

> برنامهٔ تغییر پارتیشن‌ها.
> همچنین : `partprobe`.
> اطلاعات بیشتر: <https://www.gnu.org/software/parted/parted.html>.

- شروع حالت تعاملی با دیسک مشخص انتخاب‌شده:

`sudo parted {{/dev/sdX}}`

- [تعاملی] نمایش اطلاعات پارتیشن در حالت تعاملی:

`print`

- [تعاملی] انتخاب دیسک در حالت تعاملی:

`select {{/dev/sdX}}`

- [تعاملی] ایجاد پارتیشن ۱۶ گیگابایتی با فایل‌سیستم مشخص در حالت تعاملی (جدول پارتیشن `GPT`):

`mkpart {{partition_name}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- [تعاملی] ایجاد پارتیشن ۱۶ گیگابایتی با فایل‌سیستم مشخص در حالت تعاملی (جدول پارتیشن `MBR`):

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- [تعاملی] تغییر اندازهٔ پارتیشن در حالت تعاملی:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- [تعاملی] حذف پارتیشن در حالت تعاملی:

`rm {{/dev/sdXN}}`

- [تعاملی] نمایش راهنما:

`?`
