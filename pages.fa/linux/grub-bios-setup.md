# grub-bios-setup

> آماده‌سازی دستگاه برای استفاده از GRUB با پیکربندی BIOS.
> در بیشتر موارد باید به جای `grub-bios-setup` از `grub-install` استفاده کنید.
> اطلاعات بیشتر: <https://manned.org/grub-bios-setup>.

- آماده‌سازی دستگاه برای راه‌اندازی با GRUB:

`grub-bios-setup {{/dev/sdX}}`

- نصب حتی در صورت تشخیص مشکل:

`grub-bios-setup {{[-f|--force]}} {{/dev/sdX}}`

- نصب GRUB در دایرکتوری مشخص:

`grub-bios-setup {{[-d|--directory]}} {{/boot/grub}} {{/dev/sdX}}`
