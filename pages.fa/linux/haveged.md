# haveged

> تولیدکنندهٔ اعداد تصادفی مبتنی بر سخت‌افزار.
> اطلاعات بیشتر: <https://manned.org/haveged>.

- تولید عدد تصادفی:

`sudo haveged`

- اجرای `haveged` در پیش‌زمینه:

`sudo haveged {{[-F|--Foreground]}}`

- تنظیم مسیر فایل خروجی `haveged`:

`sudo haveged {{[-f|--file]}} {{path/to/file}}`

- تنظیم سطح اجرای سرویس:

`sudo haveged {{[-r|--run]}} {{runlevel}}`

- تنظیم اندازهٔ بافر جمع‌آوری بر حسب واژه‌های کیبی‌بایتی:

`sudo haveged {{[-b|--buffer]}} {{buffer_size_in_kw}}`

- ارسال دستور به فرایند یا سرویس `haveged` در حال اجرا:

`sudo haveged {{[-c|--command]}} {{command}}`

- تنظیم اندازهٔ حافظهٔ نهان بر حسب واژه‌های کیبی‌بایتی:

`sudo haveged {{[-d|--data]}} {{cache_size_in_kw}}`

- تنظیم تعداد بایت‌های نوشتنی در فایل خروجی:

`sudo haveged {{[-n|--number]}} {{byteamount}}`
