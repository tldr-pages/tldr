# cryptsetup

> مدیریت حجم‌های رمزگذاری‌شدهٔ سادهٔ `dm-crypt` و LUKS (Linux Unified Key Setup).
> برخی زیردستورها مانند `luksFormat` مستندات استفادهٔ جداگانه دارند.
> اطلاعات بیشتر: <https://manned.org/cryptsetup>.

- مقداردهی اولیهٔ یک حجم LUKS با عبارت عبور (همهٔ داده‌های پارتیشن را بازنویسی می‌کند):

`cryptsetup luksFormat {{/dev/sdXY}}`

- باز کردن یک حجم LUKS و ایجاد نگاشت رمزگشایی‌شده در `/dev/mapper/mapping_name`:

`cryptsetup open {{/dev/sdXY}} {{mapping_name}}`

- نمایش اطلاعات یک نگاشت:

`cryptsetup status {{mapping_name}}`

- حذف یک نگاشت موجود:

`cryptsetup close {{mapping_name}}`

- تغییر عبارت عبور یک حجم LUKS:

`cryptsetup luksChangeKey {{/dev/sdXY}}`

- نمایش اطلاعات سربرگ LUKS و فرادادهٔ جایگاه‌های کلید یک دستگاه رمزگذاری‌شده:

`cryptsetup luksDump {{/dev/sdXY}}`
