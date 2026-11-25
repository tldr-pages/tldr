# zramctl

> راه‌اندازی و کنترل دستگاه‌های zram.
> از `mkfs` یا `mkswap` برای قالب‌بندی دستگاه‌های zram به پارتیشن استفاده کنید.
> اطلاعات بیشتر: <https://manned.org/zramctl>.

- بررسی فعال بودن zram:

`lsmod | grep {{[-i|--ignore-case]}} zram`

- فعال کردن zram با تعداد پویای دستگاه‌ها (برای پیکربندی بیشتر دستگاه‌ها از `zramctl` استفاده کنید):

`sudo modprobe zram`

- فعال کردن zram با دقیقاً ۲ دستگاه:

`sudo modprobe zram num_devices=2`

- یافتن و مقداردهی اولیهٔ دستگاه آزاد بعدی zram به‌صورت درایو مجازی ۲ گیگابایتی با فشرده‌سازی LZ4:

`sudo zramctl {{[-f|--find]}} {{[-s|--size]}} 2GB {{[-a|--algorithm]}} lz4`

- فهرست کردن دستگاه‌های مقداردهی‌شدهٔ فعلی:

`sudo zramctl`
