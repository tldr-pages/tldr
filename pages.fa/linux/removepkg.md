# removepkg

> حذف بستهٔ مشخص Slackware.
> اطلاعات بیشتر: <https://www.slackbook.org/html/book.html#PACKAGE-MANAGEMENT-PACKAGE-UTILITIES-REMOVEPKG>.

- حذف بسته:

`sudo removepkg {{package_name}}`

- تولید گزارش حذف شبیه‌سازی‌شده در `stdout`:

`removepkg -warn {{package_name}}`

- بازسازی زیردرخت بسته در `/tmp/preserved_packages/package_name` و حذف بسته:

`sudo removepkg -preserve {{package_name}}`

- کپی بسته زیر `/tmp/preserved_packages/package_name` بدون حذف:

`removepkg -copy {{package_name}}`

- ذخیرهٔ فایل‌های موقت ایجادشده توسط `removepkg` برای اشکال‌زدایی:

`sudo removepkg -keep {{package_name}}`
