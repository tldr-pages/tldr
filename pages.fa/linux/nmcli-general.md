# nmcli general

> مدیریت تنظیمات عمومی NetworkManager.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#general>.

- نمایش وضعیت عمومی NetworkManager:

`nmcli {{[g|general]}}`

- نمایش نام میزبان دستگاه فعلی:

`nmcli {{[g|general]}} {{[h|hostname]}}`

- تغییر نام میزبان دستگاه فعلی:

`sudo nmcli {{[g|general]}} {{[h|hostname]}} {{new_hostname}}`

- نمایش مجوزهای NetworkManager:

`nmcli {{[g|general]}} {{[p|permissions]}}`

- نمایش سطح و حوزه‌های فعلی ثبت گزارش:

`nmcli {{[g|general]}} {{[l|logging]}}`

- تنظیم سطح و یا حوزه‌های ثبت گزارش (برای همهٔ حوزه‌های موجود `man NetworkManager.conf` را ببینید):

`sudo nmcli {{[g|general]}} {{[l|logging]}} {{[l|level]}} {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domain_1,domain_2,...}}`
