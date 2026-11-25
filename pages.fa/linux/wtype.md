# wtype

> شبیه‌سازی ورودی صفحه‌کلید در Wayland، مشابه `xdotool type` برای X11.
> همچنین : `ydotool`.
> اطلاعات بیشتر: <https://manned.org/wtype>.

- شبیه‌سازی تایپ متن:

`wtype "{{Hello World}}"`

- تایپ کلید مشخص:

`wtype -k {{Left}}`

- فشردن کلید تغییردهنده:

`wtype -M {{shift|ctrl|...}}`

- رها کردن کلید تغییردهنده:

`wtype -m {{ctrl}}`

- انتظار بین فشردن کلیدها (بر حسب میلی‌ثانیه):

`wtype -d {{500}} -- "{{text}}"`

- خواندن متن از `stdin`:

`echo "{{text}}" | wtype -`
