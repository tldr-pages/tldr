# synopkg

> ابزار مدیریت بسته برای Synology DiskStation Manager.
> اطلاعات بیشتر: <https://www.synology.com/dsm>.

- فهرست کردن نام بسته‌های نصب‌شده:

`synopkg list --name`

- فهرست کردن بسته‌های وابسته به بستهٔ مشخص:

`synopkg list --depend-on {{package}}`

- شروع یا توقف بسته:

`sudo synopkg {{start|stop}} {{package}}`

- چاپ وضعیت بسته:

`synopkg status {{package}}`

- حذف بسته:

`sudo synopkg uninstall {{package}}`

- بررسی وجود به‌روزرسانی برای بسته:

`synopkg checkupdate {{package}}`

- ارتقای همهٔ بسته‌ها به جدیدترین نسخه:

`sudo synopkg upgradeall`

- نصب بسته از فایل synopkg:

`sudo synopkg install {{path/to/package.spk}}`
