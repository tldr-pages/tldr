# chat

> خودکارسازی تبادل پیام با مودم یا دستگاه سریال.
> معمولاً برای برقراری اتصال‌های PPP (پروتکل نقطه‌به‌نقطه) استفاده می‌شود.
> اطلاعات بیشتر: <https://manned.org/chat>.

- اجرای مستقیم یک اسکریپت chat:

`chat '{{expect_send_pairs}}'`

- اجرای یک اسکریپت chat از فایل:

`chat -f '{{path/to/chat_script}}'`

- تنظیم مهلت زمانی دلخواه برای انتظار پاسخ، بر حسب ثانیه:

`chat -t {{timeout_in_seconds}} '{{expect_send_pairs}}'`

- فعال کردن خروجی مفصل برای ثبت مکالمه در `syslog`:

`chat -v '{{expect_send_pairs}}'`

- استفاده از یک فایل گزارش برای ثبت رشته‌های مشخص دریافت‌شده در طول مکالمه:

`chat -r {{path/to/report_file}} '{{expect_send_pairs}}'`

- شماره‌گیری یک شماره تلفن با استفاده از متغیری که جایگزین `\T` در اسکریپت می‌شود:

`chat -T '{{phone_number}}' '{{"ATDT\\T CONNECT"}}'`

- افزودن شرط توقف در صورت دریافت یک رشتهٔ مشخص:

`chat 'ABORT "{{error_string}}" {{expect_send_pairs}}'`
