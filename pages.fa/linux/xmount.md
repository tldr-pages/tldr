# xmount

> تبدیل هم‌زمان بین انواع تصاویر ورودی و خروجی دیسک سخت با پشتیبانی اختیاری از حافظهٔ نهان نوشتن.
> ایجاد فایل‌سیستم مجازی با FUSE (فایل‌سیستم در فضای کاربر) حاوی نمایش مجازی تصویر ورودی.
> اطلاعات بیشتر: <https://manned.org/xmount>.

- سوار کردن فایل تصویر `.raw` در فایل کانتینر DMG:

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{path/to/mount_point}}`

- سوار کردن فایل تصویر EWF با پشتیبانی حافظهٔ نهان نوشتن در فایل VHD برای راه‌اندازی از آن:

`xmount --cache {{path/to/cache.ovl}} --in {{ewf}} {{path/to/image.E??}} --out {{vhd}} {{path/to/mount_point}}`

- سوار کردن نخستین پارتیشن در سکتور ۲۰۴۸ در فایل تصویر `.raw` جدید:

`xmount --offset 2048 --in {{raw}} {{path/to/image.dd}} --out raw {{path/to/mount_point}}`
