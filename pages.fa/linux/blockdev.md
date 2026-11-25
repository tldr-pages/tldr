# blockdev

> مدیریت، پرس‌وجو و تغییر دستگاه‌های بلوکی.
> اطلاعات بیشتر: <https://manned.org/blockdev>.

- چاپ گزارش همهٔ دستگاه‌ها:

`sudo blockdev --report`

- چاپ گزارش یک دستگاه مشخص:

`sudo blockdev --report {{/dev/sdXY}}`

- دریافت اندازهٔ یک دستگاه بر حسب سکتورهای ۵۱۲ بایتی:

`sudo blockdev --getsz {{/dev/sdXY}}`

- تنظیم حالت فقط‌خواندنی:

`sudo blockdev --setro {{/dev/sdXY}}`

- تنظیم حالت خواندن و نوشتن:

`sudo blockdev --setrw {{/dev/sdXY}}`

- تخلیهٔ بافرها:

`sudo blockdev --flushbufs {{/dev/sdXY}}`

- دریافت اندازهٔ بلوک فیزیکی:

`sudo blockdev --getpbsz {{/dev/sdXY}}`

- تنظیم مقدار پیش‌خوانی روی ۱۲۸ سکتور:

`sudo blockdev --setra 128 {{/dev/sdXY}}`
