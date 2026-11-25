# mhwd

> ابزار شناسایی سخت‌افزار Manjaro.
> اطلاعات بیشتر: <https://wiki.manjaro.org/index.php/Manjaro_Hardware_Detection_Overview>.

- فهرست کردن درایورهای موجود:

`mhwd {{[-l|--list]}}`

- فهرست کردن درایورهای نصب‌شده:

`mhwd {{[-li|--listinstalled]}}`

- نصب درایور:

`mhwd {{[-i|--install]}} {{pci|usb}} {{driver_name}}`

- حذف درایور:

`mhwd {{[-r|--remove]}} {{pci|usb}} {{driver_name}}`

- نمایش اطلاعات مفصل سخت‌افزار شناسایی‌شده:

`mhwd {{[-l|--list]}} {{[-d|--detail]}}`

- نصب خودکار بهترین درایور موجود برای کارت گرافیک شناسایی‌شده:

`mhwd {{[-a|--auto]}} pci {{free|nonfree}} 0300`
