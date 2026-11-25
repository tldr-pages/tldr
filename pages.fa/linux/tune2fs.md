# tune2fs

> تنظیم پارامترهای فایل‌سیستم ext2، ext3 یا ext4.
> روی فایل‌سیستم‌های سوارشده قابل استفاده است.
> اطلاعات بیشتر: <https://manned.org/tune2fs>.

- تنظیم حداکثر تعداد دفعات پیش از بررسی فایل‌سیستم به ۲:

`sudo tune2fs -c 2 {{/dev/sdXN}}`

- تنظیم برچسب فایل‌سیستم به `MY_LABEL`:

`sudo tune2fs -L 'MY_LABEL' {{/dev/sdXN}}`

- فعال کردن discard و ویژگی‌های گستردهٔ مشخص‌شده توسط کاربر برای فایل‌سیستم:

`sudo tune2fs -o discard,user_xattr {{/dev/sdXN}}`

- فعال کردن journaling برای فایل‌سیستم:

`sudo tune2fs -o has_journal {{/dev/sdXN}}`

- اختصاص UUID تصادفی جدید به فایل‌سیستم:

`sudo tune2fs -U random {{/dev/sdXN}}`
