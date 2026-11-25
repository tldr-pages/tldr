# xfreerdp3

> پیاده‌سازی آزاد پروتکل دسکتاپ راه دور (نسخهٔ ۳).
> اطلاعات بیشتر: <https://manned.org/xfreerdp3>.

- اتصال به سرور FreeRDP:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}}`

- اتصال به سرور در حالت تمام‌صفحه:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /f`

- اتصال به سرور با عرض و ارتفاع دلخواه نمایشگر:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /w:{{width_in_pixels}} /h:{{height_in_pixels}}`

- اتصال به سرور با مقیاس‌بندی پویای وضوح:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /dynamic-resolution`

- اتصال به سرور با هدایت کلیپ‌بورد:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} +clipboard`

- اتصال به سرور با دامنهٔ مشخص:

`xfreerdp3 /u:{{username}} /p:{{password}} /d:{{domain}} /v:{{host}}`

- اتصال به سرور با نادیده گرفتن بررسی‌های گواهی:

`xfreerdp3 /u:{{username}} /p:{{password}} /v:{{host}} /cert:ignore`
