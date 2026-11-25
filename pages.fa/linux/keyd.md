# keyd

> بازنگاشت کلیدها.
> اطلاعات بیشتر: <https://manned.org/keyd>.

- شروع و فعال کردن سرویس `keyd`:

`systemctl enable keyd --now`

- نمایش اطلاعات فشردن کلید:

`sudo keyd {{[-m|monitor]}}`

- بازنشانی نگاشت‌ها و بارگذاری مجدد فایل‌های پیکربندی در `/etc/keyd`:

`sudo keyd reload`

- فهرست کردن همهٔ نام‌های معتبر کلیدها:

`keyd list-keys`

- بررسی خطاهای فایل‌های پیکربندی شناسایی‌شده:

`keyd check`

- ایجاد نگاشت موقت:

`sudo keyd bind "{{pressed_key}} = {{output_key}}"`
