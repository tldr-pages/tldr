# dkms

> چارچوبی برای ساخت پویای ماژول‌های هسته.
> اطلاعات بیشتر: <https://manned.org/dkms>.

- فهرست کردن ماژول‌های نصب‌شدهٔ فعلی:

`dkms status`

- بازسازی همهٔ ماژول‌ها برای هستهٔ در حال اجرا:

`sudo dkms autoinstall`

- نصب نسخهٔ 1.2.1 ماژول acpi_call برای هستهٔ در حال اجرا:

`sudo dkms install -m acpi_call -v 1.2.1`

- حذف نسخهٔ 1.2.1 ماژول acpi_call از همهٔ هسته‌ها:

`sudo dkms remove -m acpi_call -v 1.2.1 --all`
