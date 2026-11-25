# pct set

> تنظیم گزینه‌های کانتینر.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_set>.

- تنظیم کانتینر برای شروع خودکار هنگام راه‌اندازی:

`pct {{[se|set]}} {{100}} --onboot`

- تنظیم IP ایستا برای کانتینر:

`pct {{[se|set]}} {{100}} --net0 name=eth0,bridge=vmbr0,ip={{10.0.0.100/24}},gw={{10.0.0.1}}`

- تنظیم محدودیت حافظه و CPU کانتینر:

`pct {{[se|set]}} {{100}} --memory {{8192}} --cpulimit {{4}}`

- تنظیم نام میزبان کانتینر:

`pct {{[se|set]}} {{100}} --hostname {{new_name}}`

- سوار کردن محل فایل میزبان در مهمان:

`pct {{[se|set]}} {{100}} --mp{{0}} /{{path/to/host_directory}},mp=/{{path/to/guest_mount_point}}`

- تنظیم برچسب‌های کانتینر:

`pct {{[se|set]}} {{100}} --tags {{tag1,tag2,...}}`

- حذف گزینه:

`pct {{[se|set]}} {{100}} --delete {{unused0,net0,mp0,mp1,...}}`
