# uvcdynctrl

> مدیریت کنترل‌های پویای uvcvideo.
> اطلاعات بیشتر: <https://manned.org/uvcdynctrl>.

- فهرست کردن همهٔ دوربین‌های موجود:

`uvcdynctrl {{[-l|--list]}}`

- استفاده از دستگاه مشخص (پیش‌فرض `video0`):

`uvcdynctrl {{[-d|--device]}} {{device_name}}`

- فهرست کردن کنترل‌های موجود:

`uvcdynctrl {{[-c|--clist]}}`

- تنظیم مقدار کنترل جدید (برای مقادیر منفی از `-- -value` استفاده کنید):

`uvcdynctrl {{[-s|--set]}} {{control_name}} {{value}}`

- دریافت مقدار فعلی کنترل:

`uvcdynctrl {{[-g|--get]}} {{control_name}}`

- ذخیرهٔ وضعیت کنترل‌های فعلی در فایل:

`uvcdynctrl {{[-W|--save]}} {{filename}}`

- بارگذاری وضعیت کنترل‌ها از فایل:

`uvcdynctrl {{[-L|--load]}} {{filename}}`
