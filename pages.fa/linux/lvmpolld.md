# lvmpolld

> سرویس پایش LVM که بر عملیات طولانی‌مدت LVM نظارت می‌کند.
> اطلاعات بیشتر: <https://manned.org/lvmpolld>.

- شروع سرویس در پیش‌زمینه:

`lvmpolld {{[-f|--foreground]}}`

- شروع در پیش‌زمینه با ثبت گزارش اشکال‌زدایی:

`lvmpolld {{[-f|--foreground]}} {{[-l|--log]}} debug`

- تنظیم مهلت خاموشی هنگام بی‌کاری (ثانیه):

`lvmpolld {{[-t|--timeout]}} {{300}}`

- استفاده از مسیر سوکت دلخواه:

`lvmpolld {{[-s|--socket]}} {{/tmp/lvmpolld.socket}}`

- استفاده از فایل PID دلخواه:

`lvmpolld {{[-p|--pidfile]}} {{/tmp/lvmpolld.pid}}`

- چاپ وضعیت فعلی:

`lvmpolld --dump`
