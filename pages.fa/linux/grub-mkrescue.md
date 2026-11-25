# grub-mkrescue

> ساخت تصویر قابل راه‌اندازی CD، USB یا فلاپی GRUB.
> اطلاعات بیشتر: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmkrescue>.

- ایجاد ISO قابل راه‌اندازی از دایرکتوری فعلی و ذخیرهٔ آن با نام `grub.iso`:

`grub-mkrescue --output {{grub.iso}} .`

- ایجاد ISO با فایل‌های GRUB از دایرکتوری دلخواه:

`grub-mkrescue --directory {{/usr/lib/grub/i386-pc}} --output {{grub.iso}} {{path/to/source}}`

- استفاده از فشرده‌سازی برای فایل‌های GRUB هنگام ساخت تصویر؛ مقدار `no` فشرده‌سازی را غیرفعال می‌کند:

`grub-mkrescue --compress {{no|xz|gz|lzo}} --output {{grub.iso}} {{path/to/source}}`

- غیرفعال کردن رابط خط فرمان GRUB در تصویر تولیدشده:

`grub-mkrescue --disable-cli --output {{grub.iso}} {{path/to/source}}`

- پیش‌بارگذاری ماژول‌های مشخص GRUB در تصویر:

`grub-mkrescue --modules "{{part_gpt iso9660}}" --output {{grub.iso}} {{path/to/source}}`

- ارسال مستقیم گزینه‌های اضافی به `xorriso`:

`grub-mkrescue --output {{grub.iso}} -- {{-volid}} {{volume_name}} {{path/to/source}}`

- نمایش راهنما:

`grub-mkrescue {{[-?|--help]}}`

- نمایش نسخه:

`grub-mkrescue --version`
