# fonttools subset

> تولید زیرمجموعهٔ قلم‌ها یا بهینه‌سازی اندازهٔ فایل‌ها.
> اطلاعات بیشتر: <https://fonttools.readthedocs.io/en/latest/subset/index.html>.

- محدود کردن فایل قلم TTF به بلوک Basic Latin یونیکد:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F`

- تغییر نوع فایل به WOFF2:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F --flavor=woff2`

- نگه داشتن فقط قابلیت‌های قلم OpenType به نام onum (اعداد قدیمی) و kern (فاصله‌گذاری جفت‌حروف):

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F --layout-features=onum,kern`

- تنظیم نام فایل خروجی:

`fonttools subset {{path/to/font.ttf}} --unicodes=U+0000-007F --output-file={{path/to/subset.ttf}}`
