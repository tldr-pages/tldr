# rtcwake

> ورود به وضعیت خواب سیستم تا زمان بیداری مشخص نسبت به ساعت BIOS.
> اطلاعات بیشتر: <https://manned.org/rtcwake>.

- نمایش تنظیم بودن یا نبودن هشدار:

`sudo rtcwake {{[-m|--mode]}} show {{[-v|--verbose]}}`

- تعلیق در RAM و بیدار شدن پس از ۱۰ ثانیه:

`sudo rtcwake {{[-m|--mode]}} mem {{[-s|--seconds]}} 10`

- تعلیق روی دیسک (صرفه‌جویی توان بیشتر) و بیدار شدن ۱۵ دقیقه بعد:

`sudo rtcwake {{[-m|--mode]}} disk --date +15min`

- انجماد سیستم (کارآمدتر از تعلیق در RAM اما نیازمند نسخهٔ ۳٫۹ یا جدیدتر هستهٔ لینوکس) و بیداری در تاریخ و زمان مشخص:

`sudo rtcwake {{[-m|--mode]}} freeze --date {{YYYYMMDDhhmm}}`

- غیرفعال کردن هشدار ازپیش‌تنظیم‌شده:

`sudo rtcwake {{[-m|--mode]}} disable`

- شبیه‌سازی بیدار شدن رایانه در زمان مشخص (برای لغو `<Ctrl c>` را فشار دهید):

`sudo rtcwake {{[-m|--mode]}} on --date {{hh:ss}}`
