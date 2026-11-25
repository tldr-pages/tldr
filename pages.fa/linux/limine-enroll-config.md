# limine-enroll-config

> درج یا بازنشانی هش BLAKE2B فایل `limine.conf` در فایل اجرایی EFI مربوط به Limine.
> برای اطمینان از دستکاری نشدن فایل پیکربندی هنگام فعال بودن Secure Boot استفاده می‌شود.
> اطلاعات بیشتر: <https://codeberg.org/Limine/Limine/src/branch/trunk/USAGE.md#secure-boot>.

- درج هش BLAKE2B فایل پیکربندی در فایل اجرایی EFI مربوط به Limine:

`limine-enroll-config {{path/to/BOOTX64.EFI}} {{blake2b_hash}}`

- حذف هش ثبت‌شده از فایل اجرایی و غیرفعال کردن بررسی صحت پیکربندی:

`limine-enroll-config --reset {{path/to/BOOTX64.EFI}}`

- نمایش راهنما:

`limine-enroll-config --help`
