# service

> مدیریت سرویس‌ها با اجرای اسکریپت‌های init.
> مسیر کامل اسکریپت باید حذف شود (`/etc/init.d/` فرض می‌شود).
> اطلاعات بیشتر: <https://manned.org/service>.

- فهرست کردن نام و وضعیت همهٔ سرویس‌ها:

`service --status-all`

- شروع، توقف، راه‌اندازی مجدد یا بارگذاری مجدد سرویس (شروع و توقف باید همیشه در دسترس باشند):

`service {{service_name}} {{start|stop|restart|reload}}`

- راه‌اندازی مجدد کامل (اجرای اسکریپت دو بار با توقف و شروع):

`service {{service_name}} --full-restart`

- نمایش وضعیت فعلی سرویس:

`service {{service_name}} status`
