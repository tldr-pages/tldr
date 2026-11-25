# systemd-cryptenroll

> ثبت یا حذف تعاملی روش‌های باز کردن دستگاه‌های رمزگذاری‌شده با LUKS2. مگر خلاف آن مشخص شود از رمز عبور برای باز کردن استفاده می‌کند.
> برای باز شدن پارتیشن هنگام راه‌اندازی، فایل `/etc/crypttab` یا initramfs را به‌روزرسانی کنید.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-cryptenroll.html>.

- ثبت رمز عبور جدید (مانند `cryptsetup luksAddKey`):

`systemd-cryptenroll --password {{path/to/luks2_block_device}}`

- ثبت کلید بازیابی جدید (عبارت عبور تصادفی قابل استفاده در مواقع اضطراری):

`systemd-cryptenroll --recovery-key {{path/to/luks2_block_device}}`

- فهرست کردن توکن‌های موجود یا ثبت توکن جدید PKCS#11:

`systemd-cryptenroll --pkcs11-token-uri {{list|auto|pkcs11_token_uri}} {{path/to/luks2_block_device}}`

- فهرست کردن دستگاه‌های موجود FIDO2 یا ثبت دستگاه جدید FIDO2 (وقتی فقط یک توکن متصل است می‌توان از `auto` به‌عنوان نام دستگاه استفاده کرد):

`systemd-cryptenroll --fido2-device {{list|auto|path/to/fido2_hidraw_device}} {{path/to/luks2_block_device}}`

- ثبت دستگاه جدید FIDO2 با تأیید کاربر (زیست‌سنجی):

`systemd-cryptenroll --fido2-device {{auto|path/to/fido2_hidraw_device}} --fido2-with-user-verification yes {{path/to/luks2_block_device}}`

- باز کردن با دستگاه FIDO2 و ثبت دستگاه جدید FIDO2:

`systemd-cryptenroll --unlock-fido2-device {{path/to/fido2_hidraw_unlock_device}} --fido2-device {{path/to/fido2_hidraw_enroll_device}} {{path/to/luks2_block_device}}`

- ثبت تراشهٔ امنیتی TPM2 (فقط PCR سیاست راه‌اندازی امن) و الزام PIN حروف و اعداد اضافی:

`systemd-cryptenroll --tpm2-device {{auto|path/to/tpm2_block_device}} --tpm2-with-pin yes {{path/to/luks2_block_device}}`

- حذف همهٔ رمزهای خالی، همهٔ رمزها، دستگاه‌های FIDO2، توکن‌های PKCS#11، تراشه‌های TPM2، کلیدهای بازیابی یا همهٔ روش‌ها:

`systemd-cryptenroll --wipe-slot {{empty|password|fido2|pkcs#11|tpm2|recovery|all}} {{path/to/luks2_block_device}}`
