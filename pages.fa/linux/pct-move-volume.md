# pct move-volume

> انتقال حجم به فضای ذخیره‌سازی دیگر یا کانتینر دیگر.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_move-volume>.

- انتقال فایل‌سیستم ریشهٔ کانتینر به فضای ذخیره‌سازی دیگر:

`pct {{[mov|move-volume]}} {{100}} rootfs {{storage_id}}`

- حذف ارتباط فایل‌سیستم با حجم قدیمی پس از تکمیل انتقال:

`pct {{[mov|move-volume]}} {{100}} rootfs {{storage_id}} --delete`
