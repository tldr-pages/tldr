# ufw app

> مدیریت پروفایل‌های برنامهٔ `ufw` و قوانین دیوار آتش مرتبط.
> پروفایل‌های برنامه در `/etc/ufw/applications.d/` تعریف می‌شوند.
> اطلاعات بیشتر: <https://manned.org/ufw#head8>.

- فهرست کردن پروفایل‌های برنامهٔ موجود:

`sudo ufw app list`

- نمایش اطلاعات پروفایل مشخص یا همهٔ پروفایل‌ها:

`sudo ufw app info {{profile_name|all}}`

- اجازه یا منع ترافیک با پروفایل مشخص:

`sudo ufw {{allow|deny}} "{{profile_name}}"`

- به‌روزرسانی قوانین دیوار آتش برای پروفایل تغییریافته یا همهٔ پروفایل‌ها:

`sudo ufw app update {{profile_name|all}}`

- به‌روزرسانی پروفایل و افزودن قوانین جدید در صورت نبود:

`sudo ufw app update --add-new "{{profile_name}}"`

- پیکربندی رفتار پیش‌فرض `update --add-new`:

`sudo ufw app default {{allow|deny|reject|skip}}`
