# grub-reboot

> تنظیم ورودی پیش‌فرض راه‌اندازی GRUB فقط برای راه‌اندازی بعدی.
> اطلاعات بیشتر: <https://manned.org/grub-reboot>.

- تنظیم ورودی پیش‌فرض راه‌اندازی با شماره، نام یا شناسه برای راه‌اندازی بعدی:

`sudo grub-reboot {{entry_number}}`

- تنظیم ورودی پیش‌فرض راه‌اندازی با شماره، نام یا شناسه برای دایرکتوری راه‌اندازی جایگزین در راه‌اندازی بعدی:

`sudo grub-reboot --boot-directory /{{path/to/boot_directory}} {{entry_number}}`
