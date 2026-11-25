# pct resize

> تغییر اندازهٔ فضای ذخیره‌سازی کانتینر.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_resize>.

- تغییر اندازهٔ کانتینر به ۲۰ گیگابایت:

`pct {{[resi|resize]}} {{100}} rootfs 20G`

- افزودن ۱۰ گیگابایت به فضای ذخیره‌سازی کانتینر:

`pct {{[resi|resize]}} {{100}} rootfs +10G`

- تغییر اندازهٔ حجم سوارشده:

`pct {{[resi|resize]}} {{100}} mp{{0}} {{+10G}}`
