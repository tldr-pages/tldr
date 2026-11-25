# systemd-cgtop

> نمایش گروه‌های کنترل برتر سلسله‌مراتب محلی لینوکس، مرتب‌شده بر اساس بار CPU، حافظه یا ورودی/خروجی دیسک.
> همچنین ببینید: `top`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-cgtop.html>.

- شروع نمای تعاملی:

`systemd-cgtop`

- تغییر ترتیب مرتب‌سازی:

`systemd-cgtop --order {{cpu|memory|path|tasks|io}}`

- نمایش مصرف CPU بر حسب زمان به‌جای درصد:

`systemd-cgtop --cpu=percentage`

- تغییر فاصلهٔ به‌روزرسانی بر حسب ثانیه (یا واحدهای `ms`، `us`، `min`):

`systemd-cgtop {{[-d|--delay]}} {{interval}}`

- شمارش فقط فرایندهای فضای کاربر (بدون رشته‌های هسته):

`systemd-cgtop -P`
