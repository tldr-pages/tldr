# abrt-cli

> ابزار گزارش خودکار خطا برای سیستم‌های مبتنی بر فدورا.
> برای تشخیص، تحلیل و گزارش خرابی برنامه‌ها استفاده می‌شود.
> اطلاعات بیشتر: <https://abrt.readthedocs.io/en/latest/usage.html>.

- فهرست کردن مشکلات تشخیص‌داده‌شده:

`abrt-cli list`

- نمایش جزئیات یک مشکل مشخص:

`abrt-cli info {{problem_id}}`

- حذف یک گزارش خرابی:

`abrt-cli remove {{problem_id}}`

- گزارش یک مشکل به سامانهٔ پیگیری خطای پیکربندی‌شده (مانند Bugzilla):

`abrt-cli report {{problem_id}}`

- نظارت بر یک فایل گزارش و اجرای یک برنامه هنگام یافتن مورد مطابق:

`abrt-watch-log -F {{error_string}} {{/var/log/myapp.log}} {{notify-send "Crash detected"}}`

- تولید دستی گزارش برای اشکال‌زدایی:

`abrt-cli report {{[-a|--analyze]}} {{problem_id}}`
