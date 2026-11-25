# limine-entry-tool

> اسکریپت کمکی برای مدیریت ورودی‌های راه‌انداز Limine در سیستم‌های UEFI.
> اطلاعات بیشتر: <https://gitlab.com/Zesko/limine-entry-tool>.

- پویش سایر ورودی‌های فعال راه‌اندازی UEFI و افزودن آن‌ها به منوی Limine:

`limine-entry-tool --scan`

- افزودن ورودی جدید راه‌اندازی هسته با initramfs و فایل هسته:

`limine-entry-tool --add "{{kernel_name}}" "{{path/to/initramfs}}" "{{path/to/vmlinuz}}"`

- افزودن ورودی جدید راه‌اندازی تصویر یکپارچهٔ هسته (UKI):

`limine-entry-tool --add-uki "{{kernel_name}}" "{{path/to/uki.efi}}"`

- حذف ورودی راه‌اندازی هسته و فایل‌های مرتبط آن از ESP:

`limine-entry-tool --remove "{{kernel_name}}"`

- حذف کل ورودی یک سیستم‌عامل با نام یا شناسهٔ ماشین آن:

`limine-entry-tool --remove-os "{{os_name|machine_id}}"`

- افزودن ورودی راه‌اندازی EFI برای راه‌انداز جایگزین (مانند Windows):

`limine-entry-tool --add-efi "{{efi_entry_name}}" "{{path/to/loader.efi}}"`
