# btrfs filesystem

> مدیریت سیستم‌های فایل btrfs.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs-filesystem.html>.

- نمایش میزان استفاده از سیستم فایل (برای نمایش اطلاعات مفصل می‌توان با دسترسی ریشه اجرا کرد):

`btrfs {{[f|filesystem]}} {{[u|usage]}} {{path/to/btrfs_mount}}`

- نمایش میزان استفاده به تفکیک دستگاه:

`sudo btrfs {{[f|filesystem]}} {{[sh|show]}} {{path/to/btrfs_mount}}`

- یکپارچه‌سازی یک فایل در سیستم فایل btrfs (هنگام اجرای ابزار حذف داده‌های تکراری از این کار خودداری کنید):

`sudo btrfs {{[f|filesystem]}} {{[de|defragment]}} {{[-v|--verbose]}} {{path/to/file}}`

- یکپارچه‌سازی بازگشتی یک دایرکتوری (از مرز زیرحجم‌ها عبور نمی‌کند):

`sudo btrfs {{[f|filesystem]}} {{[de|defragment]}} {{[-v|--verbose]}} -r {{path/to/directory}}`

- وادار کردن سیستم به همگام‌سازی بلوک‌های دادهٔ نوشته‌نشده با دیسک‌ها:

`sudo btrfs {{[f|filesystem]}} {{[sy|sync]}} {{path/to/btrfs_mount}}`

- خلاصه‌سازی بازگشتی میزان استفاده از دیسک برای فایل‌های یک دایرکتوری:

`sudo btrfs {{[f|filesystem]}} du {{[-s|--summarize]}} {{path/to/directory}}`

- ایجاد یک فایل swap:

`sudo btrfs {{[f|filesystem]}} {{[m|mkswapfile]}} --size {{8g}} --uuid {{clear|random|time|uuid_value}} {{path/to/swapfile}}`
