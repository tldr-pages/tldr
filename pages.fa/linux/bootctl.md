# bootctl

> کنترل تنظیمات راه‌اندازی میان‌افزار EFI و مدیریت بارگذار راه‌انداز.
> همچنین ببینید: `kernel-install`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/bootctl.html>.

- نمایش اطلاعات میان‌افزار سیستم و بارگذارهای راه‌انداز:

`bootctl`

- نمایش همهٔ ورودی‌های موجود بارگذار راه‌انداز:

`bootctl list`

- تنظیم یک ورودی راه‌اندازی به‌عنوان گزینهٔ پیش‌فرض:

`sudo bootctl set-default {{entry_id}}`

- تنظیم پرچم ورود به میان‌افزار سیستم در راه‌اندازی بعدی (مشابه `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- تعیین مسیر پارتیشن سیستم EFI (پیش‌فرض `/efi/`، `/boot/` یا `/boot/efi` است):

`bootctl --esp-path /{{path/to/efi_system_partition}}/`

- نصب `systemd-boot` در پارتیشن سیستم EFI:

`sudo bootctl install`

- حذف همهٔ نسخه‌های نصب‌شدهٔ `systemd-boot` از پارتیشن سیستم EFI:

`sudo bootctl remove`
