# adig

> چاپ اطلاعات دریافتی از سرورهای سامانهٔ نام دامنه (DNS).
> اطلاعات بیشتر: <https://manned.org/adig>.

- نمایش رکورد A (پیش‌فرض) از DNS برای نام میزبان:

`adig {{example.com}}`

- نمایش خروجی اضافی اشکال‌زدایی با `-d`:

`adig -d {{example.com}}`

- اتصال به یک سرور DNS مشخص با `-s`:

`adig -s {{1.2.3.4}} {{example.com}}`

- استفاده از یک درگاه TCP مشخص برای اتصال به سرور DNS:

`adig -T {{port}} {{example.com}}`

- استفاده از یک درگاه UDP مشخص برای اتصال به سرور DNS:

`adig -U {{port}} {{example.com}}`
