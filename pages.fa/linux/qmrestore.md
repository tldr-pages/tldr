# qmrestore

> بازیابی پشتیبان‌های `vzdump` مربوط به QemuServer.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qmrestore.1.html>.

- بازیابی ماشین مجازی از فایل پشتیبان مشخص روی فضای ذخیره‌سازی اصلی:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}}`

- بازنویسی ماشین مجازی موجود از فایل پشتیبان مشخص روی فضای ذخیره‌سازی اصلی:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --force true`

- بازیابی ماشین مجازی از فایل پشتیبان مشخص روی فضای ذخیره‌سازی مشخص:

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --storage {{local}}`

- شروع فوری ماشین مجازی از پشتیبان هنگام بازیابی در پس‌زمینه (فقط در Proxmox Backup Server):

`qmrestore {{path/to/vzdump-qemu-100.vma.lzo}} {{100}} --live-restore true`
