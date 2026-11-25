# mokutil

> پیکربندی کلیدهای مالک ماشین (MOK) برای Secure Boot.
> برخی عملیات، مانند فعال یا غیرفعال کردن Secure Boot یا ثبت کلیدها، به راه‌اندازی مجدد نیاز دارند.
> اطلاعات بیشتر: <https://manned.org/mokutil>.

- نمایش فعال بودن Secure Boot:

`mokutil --sb-state`

- فعال کردن Secure Boot:

`mokutil --enable-validation`

- غیرفعال کردن Secure Boot:

`mokutil --disable-validation`

- فهرست کردن کلیدهای ثبت‌شده:

`mokutil {{[-l|--list-enrolled]}}`

- ثبت کلید جدید:

`mokutil {{[-i|--import]}} {{path/to/key.der}}`

- فهرست کردن کلیدهای در انتظار ثبت:

`mokutil {{[-N|--list-new]}}`

- تنظیم میزان جزئیات خروجی shim:

`mokutil --set-verbosity true`
