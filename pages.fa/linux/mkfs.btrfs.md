# mkfs.btrfs

> ایجاد فایل‌سیستم BTRFS.
> پیش‌فرض `raid1` است که ۲ نسخه از یک بلوک داده را در ۲ دستگاه متفاوت مشخص می‌کند.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- ایجاد فایل‌سیستم Btrfs روی پارتیشن خالی:

`sudo mkfs.btrfs {{/dev/sdXY}}`

- ایجاد فایل‌سیستم btrfs روی یک دستگاه:

`sudo mkfs.btrfs {{[-m|--metadata]}} single {{[-d|--data]}} single {{/dev/sdX}}`

- ایجاد فایل‌سیستم btrfs روی چند دستگاه با raid1:

`sudo mkfs.btrfs {{[-m|--metadata]}} raid1 {{[-d|--data]}} raid1 {{/dev/sdX /dev/sdY /dev/sdZ ...}}`

- تنظیم برچسب فایل‌سیستم:

`sudo mkfs.btrfs {{[-L|--label]}} "{{label}}" {{/dev/sdX /dev/sdY ...}}`

- بازنویسی فایل‌سیستم موجود در صورت شناسایی:

`sudo mkfs.btrfs {{[-f|--force]}} {{/dev/sdX}}`
