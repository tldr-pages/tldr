# qm create

> ایجاد یا بازیابی ماشین مجازی در مدیر ماشین مجازی QEMU/KVM.
> اطلاعات بیشتر: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_create>.

- ایجاد ماشین مجازی با دسترسی به حافظهٔ ۵۱۲ MiB و ۱ هستهٔ CPU:

`qm {{[cr|create]}} {{100}}`

- نام‌گذاری ماشین مجازی و شروع خودکار آن پس از ایجاد:

`qm {{[cr|create]}} {{100}} --name {{vm_name}} --start`

- تعیین مقدار حافظه و تعداد CPUهای ماشین مجازی:

`qm {{[cr|create]}} {{100}} --memory {{8192}} --cores {{4}}`

- تعیین نوع سیستم‌عامل ماشین:

`qm {{[cr|create]}} {{100}} --ostype {{win10}}`

- جایگزینی ماشین موجود (نیازمند بایگانی آن):

`qm {{[cr|create]}} {{100}} --archive {{path/to/backup_file.tar}} --force 1`

- تعیین اسکریپتی که بسته به وضعیت ماشین مجازی خودکار اجرا می‌شود:

`qm {{[cr|create]}} {{100}} --hookscript {{path/to/script.pl}}`

- تعیین رسانهٔ نصب:

`qm {{[cr|create]}} {{100}} --cdrom {{local:iso/install-media.iso}}`

- ایجاد ماشین مجازی که به شبکهٔ میزبان پل می‌شود:

`qm {{[cr|create]}} {{100}} --net{{0}} virtio,bridge=vmbr{{0}}`
