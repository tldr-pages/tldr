# setserial

> خواندن و تغییر اطلاعات پورت سریال.
> اطلاعات بیشتر: <https://manned.org/setserial>.

- چاپ همهٔ اطلاعات دستگاه سریال مشخص:

`setserial -a {{/dev/cuaN}}`

- چاپ خلاصهٔ پیکربندی دستگاه سریال مشخص (مفید برای چاپ هنگام راه‌اندازی):

`setserial -b {{device}}`

- تنظیم پارامتر پیکربندی مشخص برای دستگاه:

`sudo setserial {{device}} {{parameter}}`

- چاپ پیکربندی فهرستی از دستگاه‌ها:

`setserial -g {{device1 device2 ...}}`
