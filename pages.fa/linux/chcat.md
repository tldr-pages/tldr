# chcat

> تغییر دستهٔ امنیتی SELinux برای فایل‌ها.
> دسته‌ها یک سطح اضافی کنترل دسترسی بر اساس MCS (امنیت چنددسته‌ای) فراهم می‌کنند.
> همچنین : `chcon`, `semanage`.
> اطلاعات بیشتر: <https://manned.org/chcat>.

- فهرست کردن همهٔ دسته‌های موجود:

`sudo chcat {{[-L|--list]}}`

- افزودن یک دسته به فایل:

`sudo chcat +{{CategoryName}} {{path/to/file}}`

- حذف یک دسته از فایل:

`sudo chcat -- -{{CategoryName}} {{path/to/file}}`

- تنظیم دسته‌های مشخص برای یک فایل (جایگزین دسته‌های موجود):

`sudo chcat {{CategoryName1,CategoryName2,...}} {{path/to/file}}`

- نمایش دسته‌های یک فایل:

`ls {{[-Z|--context]}} {{path/to/file}}`

- حذف همهٔ دسته‌ها از یک فایل:

`sudo chcat {{[-d|--delete]}} {{path/to/file}}`
