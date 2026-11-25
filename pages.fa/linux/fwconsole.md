# fwconsole

> مدیریت و پیکربندی سیستم FreePBX (سرور PBX).
> اطلاعات بیشتر: <https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>.

- بارگذاری مجدد پیکربندی‌های FreePBX:

`fwconsole reload`

- شروع Asterisk و دیگر دستورهای مورد نیاز FreePBX:

`fwconsole start`

- توقف Asterisk و دیگر دستورهای مورد نیاز FreePBX:

`fwconsole stop`

- مشاهده و به‌روزرسانی تنظیمات:

`fwconsole setting {{keyword}} {{new_value}}`

- فهرست کردن نسخه‌های پشتیبان موجود:

`fwconsole backup --list`

- فهرست کردن دستورهای موجود FreePBX:

`fwconsole list`

- تغییر مالکیت همهٔ فایل‌ها و دایرکتوری‌هایی که FreePBX نیاز دارد متعلق به کاربر apache باشند:

`fwconsole chown`
