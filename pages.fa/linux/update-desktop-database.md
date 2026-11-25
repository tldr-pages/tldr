# update-desktop-database

> ساخت پایگاه دادهٔ حافظهٔ نهان انواع MIME که فایل‌های دسکتاپ مدیریت می‌کنند.
> اطلاعات بیشتر: <https://manned.org/update-desktop-database>.

- به‌روزرسانی حافظهٔ نهان نوع MIME فایل‌های دسکتاپ برای دایرکتوری‌های استاندارد سیستم:

`sudo update-desktop-database`

- به‌روزرسانی حافظهٔ نهان برای دایرکتوری فایل دسکتاپ مشخص:

`update-desktop-database {{path/to/directory}}`

- به‌روزرسانی حافظهٔ نهان برای چند دایرکتوری:

`update-desktop-database {{path/to/directory1 path/to/directory2 ...}}`

- به‌روزرسانی حافظهٔ نهان بدون نمایش خروجی:

`update-desktop-database {{[-q|--quiet]}}`

- به‌روزرسانی حافظهٔ نهان با خروجی مفصل:

`update-desktop-database {{[-v|--verbose]}}`
