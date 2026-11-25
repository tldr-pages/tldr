# dracut

> تولید تصاویر initramfs برای راه‌اندازی هستهٔ لینوکس.
> Dracut به‌صورت پیش‌فرض از گزینه‌های فایل‌های پیکربندی در `/etc/dracut.conf`، `/etc/dracut.conf.d/*.conf` و `/usr/lib/dracut/dracut.conf.d/*.conf` استفاده می‌کند.
> اطلاعات بیشتر: <https://github.com/dracut-ng/dracut-ng/blob/main/man/dracut.8.adoc>.

- تولید تصویر initramfs برای هستهٔ فعلی بدون بازنویسی هیچ گزینه‌ای:

`dracut`

- تولید تصویر initramfs برای هستهٔ فعلی و بازنویسی تصویر موجود:

`dracut {{[-f|--force]}}`

- تولید تصویر initramfs برای یک هستهٔ مشخص:

`dracut --kver {{kernel_version}}`

- فهرست کردن ماژول‌های موجود:

`dracut --list-modules`
