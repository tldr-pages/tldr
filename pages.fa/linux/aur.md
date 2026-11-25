# aur

> ساخت بسته‌ها از AUR و مدیریت مخازن محلی.
> توجه: برای عملکرد کامل، باید یک مخزن محلی در `/etc/pacman.conf` تعریف شده و `vifm` نصب شده باشد.
> اطلاعات بیشتر: <https://github.com/aurutils/aurutils>.

- مقداردهی اولیهٔ مخزن مطابق با مسیر موجود در `/etc/pacman.conf`:

`repo-add {{path/to/database.db.tar.gz}}`

- جست‌وجوی یک بسته در پایگاه دادهٔ AUR:

`aur search {{keyword}}`

- دانلود یک یا چند بسته و وابستگی‌های آن‌ها از AUR، ساخت آن‌ها و افزودن آن‌ها به یک مخزن محلی:

`aur sync {{package1 package2 ...}}`

- فهرست کردن بسته‌های موجود در مخزن محلی:

`aur repo {{[-l|--list]}}`

- ارتقای بسته‌های مخزن محلی:

`aur sync {{[-u|--upgrades]}}`

- پاکسازی فایل‌های ساخت پس از نصب:

`aur sync {{[-C|--clean]}} {{package}}`

- نصب یک بسته بدون مشاهدهٔ تغییرات در Vim و بدون تأیید نصب وابستگی‌ها:

`aur sync --noview {{[-n|--noconfirm]}} {{package}}`

- حذف یک بسته از فرادادهٔ مخزن (خود فایل بسته حذف نمی‌شود):

`repo-remove {{path/to/database.db.tar.gz}} {{package}}`
