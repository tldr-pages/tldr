# xdotool

> خودکارسازی عملیات X11.
> اطلاعات بیشتر: <https://manned.org/xdotool>.

- دریافت شناسهٔ پنجرهٔ X برای پنجره‌های Firefox در حال اجرا:

`xdotool search --onlyvisible --name firefox`

- انجام کلیک راست ماوس (`<RightClick>`):

`xdotool click 3`

- دریافت شناسهٔ پنجرهٔ فعال فعلی:

`xdotool getactivewindow`

- تمرکز روی پنجره‌ای با شناسهٔ مشخص:

`xdotool windowfocus --sync {{12345}}`

- تایپ پیام با تأخیر ۵۰۰ میلی‌ثانیه برای هر حرف:

`xdotool type --delay 500 "{{Hello world}}"`

- فشردن کلید `<Enter>`:

`xdotool key KP_Enter`
