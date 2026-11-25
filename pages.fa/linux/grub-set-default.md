# grub-set-default

> تنظیم ورودی پیش‌فرض راه‌اندازی GRUB.
> اطلاعات بیشتر: <https://manned.org/grub-set-default>.

- تنظیم ورودی پیش‌فرض راه‌اندازی با شماره، نام یا شناسه:

`sudo grub-set-default {{entry_number}}`

- تنظیم ورودی پیش‌فرض راه‌اندازی با شماره، نام یا شناسه برای دایرکتوری راه‌اندازی جایگزین:

`sudo grub-set-default --boot-directory /{{path/to/boot_directory}} {{entry_number}}`
