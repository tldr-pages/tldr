# grub-mount

> سوار کردن فقط‌خواندنی یک سیستم فایل یا تصویر آن با درایورهای سیستم فایل GRUB.
> اطلاعات بیشتر: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmount>.

- سوار کردن دستگاه بلوکی یا تصویر سیستم فایل در نقطهٔ اتصال:

`grub-mount {{/dev/sdXY}} {{/mnt}}`

- سوار کردن پارتیشن دوم یک تصویر کامل دیسک؛ `-r` شمارهٔ پارتیشن در تصویر را مشخص می‌کند:

`grub-mount {{[-r|--root]}} {{2}} {{disk.img}} {{/mnt}}`

- سوار کردن دستگاه رمزگذاری‌شده و درخواست عبارت عبور:

`grub-mount {{[-C|--crypto]}} {{/dev/sdXY}} {{/mnt}}`

- بارگذاری کلید رمزگذاری ZFS از فایل:

`grub-mount {{[-K|--zfs-key]}} /{{path/to/zfs.key}} {{/dev/sdX}} {{/mnt}}`

- نمایش خروجی اشکال‌زدایی برای دستهٔ مطابق:

`grub-mount {{[-d|--debug]}} {{string}} {{image}} {{/mnt}}`

- فعال کردن خروجی مفصل:

`grub-mount {{[-v|--verbose]}} {{image}} {{/mnt}}`

- نمایش راهنما:

`grub-mount {{[-?|--help]}}`

- نمایش نسخه:

`grub-mount --version`
