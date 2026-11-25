# aur sync

> دانلود و ساخت خودکار بسته‌های AUR.
> توجه: برای عملکرد کامل، باید یک مخزن محلی در `/etc/pacman.conf` تعریف شده و `vifm` نصب شده باشد.
> اطلاعات بیشتر: <https://github.com/aurutils/aurutils>.

- دانلود یک یا چند بسته و وابستگی‌های آن‌ها از AUR، ساخت آن‌ها و افزودن آن‌ها به یک مخزن محلی:

`aur sync {{package1 package2 ...}}`

- ارتقای بسته‌های مخزن محلی:

`aur sync {{[-u|--upgrades]}}`

- نادیده گرفتن بسته‌های مشخص هنگام ارتقا:

`aur sync {{[-u|--upgrades]}} --ignore {{package1,package2,...}}`

- پاکسازی فایل‌های ساخت پس از نصب:

`aur sync {{[-C|--clean]}} {{package}}`

- نصب یک بسته بدون مشاهدهٔ تغییرات در Vim و بدون تأیید نصب وابستگی‌ها:

`aur sync --noview {{[-n|--noconfirm]}} {{package}}`
