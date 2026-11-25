# maim

> ابزار تصویربرداری از صفحه.
> اطلاعات بیشتر: <https://manned.org/maim>.

- گرفتن تصویر صفحه و ذخیره در مسیر مشخص:

`maim {{path/to/screenshot.png}}`

- گرفتن تصویر ناحیهٔ انتخاب‌شده:

`maim {{[-s|--select]}} {{path/to/screenshot.png}}`

- گرفتن تصویر ناحیهٔ انتخاب‌شده و ذخیره در کلیپ‌بورد (نیازمند `xclip`):

`maim {{[-s|--select]}} | xclip {{[-se|-selection]}} {{[c|clipboard]}} {{[-t|-target]}} image/png`

- گرفتن تصویر پنجرهٔ فعال فعلی (نیازمند `xdotool`):

`maim {{[-i|--window]}} $(xdotool getactivewindow) {{path/to/screenshot.png}}`
