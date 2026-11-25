# cpupower

> ابزارهای مرتبط با توان پردازنده و گزینه‌های تنظیم آن.
> اطلاعات بیشتر: <https://manned.org/cpupower>.

- چاپ اطلاعات همهٔ هسته‌ها:

`sudo cpupower {{[-c|--cpu]}} all info`

- تنظیم راهبر فرکانس همهٔ پردازنده‌ها روی حالت صرفه‌جویی در توان:

`sudo cpupower {{[-c|--cpu]}} all frequency-set --governor {{powersave}}`

- چاپ راهبرهای فرکانس موجود برای پردازندهٔ ۰:

`sudo cpupower {{[-c|--cpu]}} 0 frequency-info {{[-g|--governors]}} | grep "analyzing\|governors"`

- چاپ فرکانس پردازندهٔ ۴ از سخت‌افزار در قالب خوانا:

`sudo cpupower {{[-c|--cpu]}} 4 frequency-info {{[-w|--hwfreq]}} {{[-m|--human]}}`
