# grub-install

> نصب GRUB روی دستگاه.
> اطلاعات بیشتر: <https://www.gnu.org/software/grub/manual/grub/grub.html#Installing-GRUB-using-grub_002dinstall>.

- نصب GRUB روی سیستم BIOS:

`sudo grub-install {{path/to/device}}`

- نصب GRUB روی سیستم BIOS با تعیین معماری:

`sudo grub-install --target {{i386-pc}} {{path/to/device}}`

- نصب GRUB روی سیستم UEFI:

`sudo grub-install --efi-directory {{path/to/efi_directory}}`

- نصب GRUB روی سیستم UEFI با تعیین معماری و متن منوی راه‌اندازی:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{path/to/efi_directory}} --bootloader-id {{GRUB}}`

- نصب GRUB با پیش‌بارگذاری ماژول‌های مشخص:

`sudo grub-install --target {{x86_64-efi}} --efi-directory {{path/to/efi_directory}} --modules "{{part_gpt part_msdos}}"`

- نمایش راهنما:

`grub-install {{[-?|--help]}}`
