# mkinitfs

> تولید initramfs در Alpine Linux.
> اطلاعات بیشتر: <https://manned.org/mkinitfs>.

- تولید initramfs با ویژگی‌های مشخص‌شده در `/etc/mkinitfs/mkinitfs.conf`:

`mkinitfs`

- استفاده از فایل پیکربندی دیگر:

`mkinitfs -c {{path/to/config}}`

- فشرده‌سازی initramfs با الگوریتم فشرده‌سازی مشخص (پیش‌فرض: `gzip`):

`mkinitfs -C {{gzip|xz|zstd|lz4|none}}`

- فهرست کردن فایل‌هایی که در تصویر initramfs گنجانده خواهند شد:

`mkinitfs -l`

- فهرست کردن همهٔ ویژگی‌های موجود:

`mkinitfs -L`
