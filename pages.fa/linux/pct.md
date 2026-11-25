# pct

> مدیریت کانتینرهای LXC در Proxmox.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- فهرست کردن همهٔ کانتینرها:

`pct list`

- شروع، توقف یا راه‌اندازی مجدد کانتینر مشخص:

`pct {{start|stop|reboot}} {{100}}`

- دسترسی به پوستهٔ کانتینر مشخص:

`pct {{[en|enter]}} {{100}}`

- ایجاد کانتینر از قالب با اندازهٔ ۴ گیگابایت:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- تغییر اندازهٔ دیسک کانتینر به 20G:

`pct {{[resi|resize]}} {{100}} {{rootfs|mpX}} {{20G}}`

- نمایش پیکربندی کانتینر با تعیین شناسهٔ آن:

`pct {{[conf|config]}} {{100}}`

- گرفتن snapshot از کانتینر مشخص همراه با توضیح:

`pct {{[sn|snapshot]}} {{100}} {{my-snapshot}} --description {{My snapshot description}}`

- از بین بردن کانتینر و حذف همهٔ منابع مرتبط:

`pct {{[des|destroy]}} {{100}} --purge`
