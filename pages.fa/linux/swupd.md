# swupd

> ابزار مدیریت بسته برای Clear Linux.
> اطلاعات بیشتر: <https://github.com/clearlinux/clear-linux-documentation/blob/master/source/guides/clear/swupd.rst>.

- به‌روزرسانی به جدیدترین نسخه:

`sudo swupd update`

- نمایش نسخهٔ فعلی و بررسی وجود نسخهٔ جدیدتر:

`swupd check-update`

- فهرست کردن مجموعه‌های نصب‌شده:

`swupd bundle-list`

- یافتن مجموعهٔ حاوی بستهٔ مورد نظر:

`swupd search -b {{package}}`

- نصب مجموعهٔ جدید:

`sudo swupd bundle-add {{bundle}}`

- حذف مجموعه:

`sudo swupd bundle-remove {{bundle}}`

- اصلاح فایل‌های خراب یا گمشده:

`sudo swupd verify`
