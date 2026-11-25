# hcitool

> پایش و پیکربندی اتصال‌ها و ارسال دستورهای ویژه به دستگاه‌های بلوتوث.
> اطلاعات بیشتر: <https://manned.org/hcitool>.

- پویش دستگاه‌های بلوتوث:

`hcitool scan`

- چاپ نام دستگاه با دریافت آدرس MAC آن:

`hcitool name {{bdaddr}}`

- دریافت اطلاعات دستگاه بلوتوث راه دور:

`hcitool info {{bdaddr}}`

- بررسی کیفیت پیوند به دستگاه بلوتوث:

`hcitool lq {{bdaddr}}`

- تغییر سطح توان ارسال:

`hcitool tpl {{bdaddr}} {{0|1}}`

- نمایش سیاست پیوند:

`hcitool lp`

- درخواست احراز هویت با دستگاه مشخص:

`hcitool auth {{bdaddr}}`

- نمایش دستگاه‌های محلی:

`hcitool dev`
