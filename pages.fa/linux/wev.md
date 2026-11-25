# wev

> چاپ محتوای رویدادهای Wayland.
> اطلاعات بیشتر: <https://manned.org/wev>.

- پایش همهٔ رویدادهای Wayland رخ‌داده:

`wev`

- چاپ همهٔ رویدادهای دریافت‌شده توسط واسط مشخص Wayland:

`wev -f {{wl_keyboard}}`

- چاپ فقط رویدادهای مشخص دریافت‌شده توسط واسط Wayland:

`wev -f {{wl_keyboard}}:{{key}}`

- چاپ همه‌چیز به‌جز رویدادهای مشخص Wayland:

`wev -F {{wl_keyboard}}:{{key}}`

- نوشتن نگاشت کلید `wl_keyboards` در فایل:

`wev -M {{path/to/file}}`

- چاپ متغیرهای سراسری Wayland:

`wev -g`
