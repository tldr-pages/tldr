# hyprpicker

> انتخاب‌کنندهٔ رنگ کمینهٔ Wayland برای ترکیب‌گرهای wlroots مانند Hyprland.
> به نشست Wayland نیاز دارد؛ برای کپی خودکار در کلیپ‌بورد باید `wl-copy` نصب باشد.
> اطلاعات بیشتر: <https://wiki.hypr.land/Hypr-Ecosystem/hyprpicker/>.

- انتخاب رنگ در قالب پیش‌فرض شانزده‌شانزدهی:

`hyprpicker`

- انتخاب رنگ و چاپ در قالب مشخص:

`hyprpicker {{[-f|--format]}} {{hex|rgb|hsl|hsv|cmyk}}`

- کپی رنگ انتخاب‌شده در کلیپ‌بورد:

`hyprpicker {{[-a|--autocopy]}}`

- غیرفعال کردن خروجی رنگی و چاپ فقط متن ساده:

`hyprpicker {{[-n|--no-fancy]}}`

- ذخیرهٔ رنگ انتخاب‌شده در متغیر پوسته:

`{{color}}=$(hyprpicker {{[-f|--format]}} {{hex}})`

- نمایش راهنما:

`hyprpicker {{[-h|--help]}}`
