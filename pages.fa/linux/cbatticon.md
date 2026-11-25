# cbatticon

> یک نماد باتری سبک و سریع در سینی سیستم.
> اطلاعات بیشتر: <https://github.com/valr/cbatticon>.

- نمایش نماد باتری در سینی سیستم:

`cbatticon`

- نمایش نماد باتری و تنظیم فاصلهٔ به‌روزرسانی روی ۲۰ ثانیه:

`cbatticon {{[-u|--update-interval]}} 20`

- فهرست کردن انواع نماد موجود:

`cbatticon {{[-t|--list-icon-types]}}`

- نمایش نماد باتری با یک نوع نماد مشخص:

`cbatticon {{[-i|--icon-type]}} {{standard|notification|symbolic}}`

- فهرست کردن منابع تغذیهٔ موجود:

`cbatticon {{[-p|--list-power-supplies]}}`

- نمایش نماد باتری برای یک باتری مشخص:

`cbatticon {{BAT0}}`

- نمایش نماد باتری و تعیین دستوری که هنگام رسیدن شارژ باتری به سطح بحرانی تنظیم‌شده اجرا شود:

`cbatticon {{[-r|--critical-level]}} {{5}} {{[-c|--command-critical-level]}} {{poweroff}}`
