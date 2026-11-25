# mkinitcpio

> تولید محیط‌های دیسک اولیهٔ RAM برای راه‌اندازی هستهٔ لینوکس بر اساس پیش‌تنظیم‌های مشخص.
> اطلاعات بیشتر: <https://manned.org/mkinitcpio>.

- شبیه‌سازی تولید محیط‌های دیسک اولیهٔ RAM و چاپ عملیات احتمالی:

`mkinitcpio`

- تولید محیط‌های دیسک RAM بر اساس همهٔ پیش‌تنظیم‌های موجود (برای تولید مجدد همهٔ تصاویر initramfs پس از تغییر در `/etc/mkinitcpio.conf`):

`sudo mkinitcpio {{[-P|--allpresets]}}`

- تولید محیط دیسک RAM بر اساس پیش‌تنظیم `linux`:

`sudo mkinitcpio {{[-p|--preset]}} linux`

- تولید محیط دیسک RAM بر اساس پیش‌تنظیم `linux-lts`:

`sudo mkinitcpio {{[-p|--preset]}} linux-lts`

- تولید تصویر initramfs با فایل پیکربندی جایگزین:

`sudo mkinitcpio {{[-c|--config]}} {{path/to/mkinitcpio.conf}} {{[-g|--generate]}} {{path/to/initramfs.img}}`

- تولید تصویر initramfs برای هسته‌ای غیر از هستهٔ در حال اجرا (نسخه‌های نصب‌شدهٔ هسته در `/usr/lib/modules/` قرار دارند):

`sudo mkinitcpio {{[-k|--kernel]}} {{kernel_version}} {{[-g|--generate]}} {{path/to/initramfs.img}}`

- فهرست کردن همهٔ hookهای موجود:

`mkinitcpio {{[-L|--listhooks]}}`

- نمایش راهنمای hook مشخص:

`mkinitcpio {{[-H|--hookhelp]}} {{hook_name}}`
