# gamescope

> یک ترکیب‌گر کوچک که به‌عنوان لایهٔ بازی استفاده می‌شود.
> همچنین : `cage`.
> اطلاعات بیشتر: <https://github.com/ValveSoftware/gamescope#keyboard-shortcuts>.

- اجرای برنامه با gamescope در پایانه:

`gamescope -- {{program}}`

- اجرای بازی با gamescope از طریق Steam:

`gamescope -- %command%`

- ارتقای مقیاس بازی 720p به 1440p با مقیاس‌دهی عدد صحیح:

`gamescope {{[-h|--nested-height]}} 720 {{[-H|--output-height]}} 1440 {{[-S|--scaler]}} integer -- {{command}}`

- محدود کردن بازی با همگام‌سازی عمودی به ۳۰ فریم بر ثانیه:

`gamescope {{[-r|--nested-refresh]}} 30 -- {{command}}`

- اجرای Steam در حالت Big Picture و یکپارچه‌سازی با gamescope:

`gamescope {{[-e|--steam]}} -- /usr/bin/steam -tenfoot`

- تعیین نمایشگر ترجیحی:

`gamescope {{[-O|--prefer-output]}} {{HDMI-A-1,DP-3,...}} -- {{program}}`

- تغییر وضعیت تمام‌صفحه:

`<Super f>`

- نمایش راهنما:

`gamescope --help`
