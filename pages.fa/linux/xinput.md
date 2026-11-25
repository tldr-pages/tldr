# xinput

> فهرست کردن دستگاه‌های ورودی موجود، پرس‌وجوی اطلاعات دستگاه و تغییر تنظیمات دستگاه ورودی.
> اطلاعات بیشتر: <https://manned.org/xinput>.

- فهرست کردن همهٔ دستگاه‌های ورودی:

`xinput list`

- غیرفعال کردن ورودی:

`xinput disable {{device_id}}`

- فعال کردن ورودی:

`xinput enable {{device_id}}`

- قطع اتصال ورودی از دستگاه اصلی آن:

`xinput float {{device_id}}`

- اتصال مجدد ورودی به‌عنوان تابع دستگاه اصلی:

`xinput reattach {{device_id}} {{master_id}}`

- فهرست کردن تنظیمات دستگاه ورودی:

`xinput list-props {{device_id}}`

- تغییر تنظیم دستگاه ورودی:

`xinput set-prop {{device_id}} {{setting_id}} {{value}}`
