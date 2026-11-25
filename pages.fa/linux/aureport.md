# aureport

> تولید گزارش‌های خلاصه از گزارش‌های auditd.
> اطلاعات بیشتر: <https://manned.org/aureport>.

- نمایش خلاصه‌ای از رویدادهای auditd:

`sudo aureport`

- تولید خلاصه‌ای از رویدادهای ورود:

`sudo aureport {{[-l|--login]}}`

- فهرست کردن همهٔ گزارش‌های فراخوانی سیستم:

`sudo aureport {{[-s|--syscall]}}`

- تولید خلاصه‌ای از رویدادهای فایل اجرایی:

`sudo aureport {{[-x|--executable]}}`

- نمایش خلاصه‌ای از رویدادها برای یک بازهٔ زمانی مشخص:

`sudo aureport {{[-ts|--start]}} {{start_time}} {{[-te|--end]}} {{end_time}}`

- فهرست کردن همهٔ فایل‌های ممیزی و بازهٔ زمانی رویدادهای موجود در آن‌ها:

`sudo aureport {{[-t|--log-time]}}`

- نمایش راهنما:

`aureport --help`
