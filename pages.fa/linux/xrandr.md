# xrandr

> تنظیم اندازه، جهت یا بازتاب خروجی‌های یک صفحه.
> اطلاعات بیشتر: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- نمایش وضعیت فعلی سیستم (نمایشگرهای شناخته‌شده، وضوح‌ها و غیره):

`xrandr {{[-q|--query]}}`

- غیرفعال کردن خروجی‌های قطع‌شده و فعال کردن خروجی‌های متصل با تنظیمات پیش‌فرض:

`xrandr --auto`

- تغییر وضوح و نرخ نوسازی DisplayPort 1 به 1920x1080 و ۶۰ هرتز:

`xrandr --output DP1 --mode 1920x1080 {{[-r|--rate]}} 60`

- تنظیم وضوح HDMI2 به 1280x1024 و قرار دادن آن در سمت راست DP1:

`xrandr --output HDMI2 --mode 1280x1024 --right-of DP1`

- غیرفعال کردن خروجی VGA1:

`xrandr --output VGA1 --off`

- تنظیم روشنایی LVDS1 به ۵۰٪:

`xrandr --output LVDS1 --brightness 0.5`

- نمایش وضعیت فعلی هر سرور X:

`xrandr {{[-d|--display]}} :{{0}} {{[-q|--query]}}`
