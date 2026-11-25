# wajig

> ابزار سادهٔ یکپارچهٔ پشتیبانی سیستم برای سیستم‌های مبتنی بر Debian.
> اطلاعات بیشتر: <https://togaware.com/linux/survivor/wajig.html>.

- به‌روزرسانی فهرست بسته‌ها و نسخه‌های موجود:

`wajig update`

- نصب بسته یا به‌روزرسانی آن به آخرین نسخهٔ موجود:

`wajig install {{package}}`

- حذف بسته و فایل‌های پیکربندی آن:

`wajig purge {{package}}`

- به‌روزرسانی فهرست و سپس اجرای dist-upgrade:

`wajig daily-upgrade`

- نمایش اندازهٔ بسته‌های نصب‌شده:

`wajig sizes`

- فهرست نسخه و توزیع همهٔ بسته‌های نصب‌شده:

`wajig versions`

- فهرست نسخه‌های بسته‌های قابل ارتقا:

`wajig toupgrade`

- نمایش بسته‌هایی که به شکلی به بستهٔ مشخص وابسته‌اند:

`wajig dependents {{package}}`
