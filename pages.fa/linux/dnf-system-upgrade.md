# dnf system-upgrade

> ارتقای فدورا به یک انتشار اصلی جدید.
> اطلاعات بیشتر: <https://dnf5.readthedocs.io/en/latest/commands/system-upgrade.8.html>.

- آماده‌سازی سیستم با ارتقای همهٔ بسته‌های نصب‌شده:

`sudo dnf upgrade --refresh`

- دانلود بسته‌های مورد نیاز برای نسخهٔ انتشار جدید:

`sudo dnf system-upgrade download --releasever {{release_version}}`

- راه‌اندازی مجدد و شروع فرایند ارتقا:

`sudo dnf system-upgrade reboot`

- نمایش وضعیت تراکنش ارتقای فعلی:

`sudo dnf system-upgrade status`

- نمایش گزارش‌های تلاش‌های قبلی ارتقا:

`sudo dnf system-upgrade log`

- حذف داده‌ها و بسته‌های ارتقای ذخیره‌شده در حافظهٔ نهان:

`sudo dnf system-upgrade clean`
