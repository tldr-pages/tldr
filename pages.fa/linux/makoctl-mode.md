# makoctl mode

> مدیریت حالت‌های اعلان در `mako`.
> از حالت‌ها می‌توان برای تغییر رفتار اعلان‌ها استفاده کرد (مانند مزاحم نشوید).
> اطلاعات بیشتر: <https://manned.org/makoctl>.

- فهرست کردن همهٔ حالت‌های فعال فعلی:

`makoctl mode`

- افزودن حالت:

`makoctl mode -a {{do-not-disturb}}`

- حذف حالت:

`makoctl mode -r {{do-not-disturb}}`

- تغییر وضعیت حالت (افزودن در صورت نبود، حذف در صورت وجود):

`makoctl mode -t {{do-not-disturb}}`

- تنظیم حالت‌های مشخص و جایگزینی همهٔ حالت‌های فعلی:

`makoctl mode -s {{mode1 mode2 ...}}`
