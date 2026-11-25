# pct create

> ایجاد کانتینرهای LXC در Proxmox.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_create>.

- ایجاد کانتینر از قالب با اندازهٔ ۴ گیگابایت، حافظهٔ ۵۱۲ MiB و دسترسی نامحدود به CPU:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- تعیین محدودیت حافظهٔ کانتینر بر حسب مگابایت:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --memory {{8192}}`

- تعیین نام میزبان و رمز عبور کانتینر:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --hostname {{hostname}} --password {{password}}`

- دادن دسترسی شبکه به کانتینر:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --net0 name={{eth0}},bridge={{vmbr0}},ip={{dhcp|manual|10.0.0.1/24}} --features nesting=1`

- شروع کانتینر بلافاصله پس از ایجاد:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --start`

- تنظیم کانتینر برای شروع هنگام راه‌اندازی سیستم:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --onboot`
