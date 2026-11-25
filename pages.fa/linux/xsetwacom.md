# xsetwacom

> تغییر تنظیمات تبلت‌های قلمی Wacom در زمان اجرا.
> اطلاعات بیشتر: <https://manned.org/xsetwacom>.

- فهرست کردن همهٔ دستگاه‌های موجود Wacom؛ نام دستگاه در ستون اول است:

`xsetwacom list`

- تنظیم ناحیهٔ Wacom برای صفحهٔ مشخص؛ نام صفحه را با `xrandr` دریافت کنید:

`xsetwacom set "{{device_name}}" MapToOutput {{screen}}`

- تنظیم حالت به نسبی (مانند ماوس) یا مطلق (مانند قلم):

`xsetwacom set "{{device_name}}" Mode "{{Relative|Absolute}}"`

- چرخاندن ورودی به اندازهٔ ۰، ۹۰، ۱۸۰ یا ۲۷۰ درجه از چرخش «طبیعی» (مفید برای تبلت‌پی‌سی هنگام چرخاندن صفحه):

`xsetwacom set "{{device_name}}" Rotate {{none|half|cw|ccw}}`

- تنظیم دکمه برای کار کردن فقط هنگامی که نوک قلم با تبلت تماس دارد:

`xsetwacom set "{{device_name}}" TabletPCButton "on"`
