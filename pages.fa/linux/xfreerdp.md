# xfreerdp

> پیاده‌سازی آزاد پروتکل دسکتاپ راه دور.
> اطلاعات بیشتر: <https://github.com/FreeRDP/FreeRDP/wiki/CommandLineInterface-(possibly-not-up-to-date,-check-application-help-text-for-most-up-to-date-version)>.

- اتصال به سرور FreeRDP:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{host}}`

- اتصال به سرور FreeRDP با عرض و ارتفاع دلخواه پنجره:

`xfreerdp /v:{{host}} /u:{{username}} /p:{{password}} /w:{{width_in_pixels}} /h:{{height_in_pixels}}`

- اتصال به سرور FreeRDP با وضوح پویا:

`xfreerdp /v:{{host}} /u:{{username}} /p:{{password}} /dynamic-resolution`

- اتصال به سرور FreeRDP با هدایت کلیپ‌بورد:

`xfreerdp /v:{{host}} /u:{{username}} /p:{{password}} +clipboard`

- اتصال به سرور FreeRDP با نادیده گرفتن همهٔ بررسی‌های گواهی:

`xfreerdp /v:{{host}} /u:{{username}} /p:{{password}} /cert:ignore`

- اتصال به سرور FreeRDP با دایرکتوری اشتراکی:

`xfreerdp /v:{{host}} /u:{{username}} /p:{{password}} /drive:{{path/to/directory}},{{share_name}}`

- اتصال به سرور FreeRDP و فعال کردن هدایت خروجی صوتی با دستگاه `sys:alsa`:

`xfreerdp /u:{{username}} /p:{{password}} /v:{{host}} /sound:{{sys:alsa}}`
