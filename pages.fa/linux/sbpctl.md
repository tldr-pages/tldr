# sbpctl

> مدیریت راه‌انداز systemd-boot-password، انشعابی از systemd-boot با ویرایشگر محافظت‌شده با رمز عبور.
> همچنین ببینید: `bootctl`.
> اطلاعات بیشتر: <https://github.com/kitsunyan/systemd-boot-password#boot-manager-installing-and-configuration>.

- نصب راه‌انداز در پارتیشن سیستمی EFI:

`sudo sbpctl install /{{path/to/efi_system_partition}}`

- نصب راه‌انداز فقط به‌عنوان بارگذار پیش‌فرض EFI (`/EFI/BOOT/BOOT*.EFI`):

`sudo sbpctl install {{[-d|--default]}} /{{path/to/efi_system_partition}}`

- نصب راه‌انداز با گنجاندن `/etc/sbp/loader.conf` در فایل دودویی EFI:

`sudo sbpctl install {{[-i|--include]}} /{{path/to/efi_system_partition}}`

- نصب راه‌انداز و امضای آن برای Secure Boot با کلیدهای موجود در `/etc/sbp`:

`sudo sbpctl install {{[-s|--sign]}} /{{path/to/efi_system_partition}}`

- تولید هش SHA-512 رمز عبور برای گزینهٔ `password` در `loader.conf`:

`sbpctl generate`

- ایجاد برنامهٔ مستقل EFI از برنامهٔ Linux EFI و initramfs:

`sudo sbpctl standalone {{[-i|--initrd]}} {{path/to/initramfs.img}} {{path/to/vmlinuz}} {{path/to/output.efi}}`
