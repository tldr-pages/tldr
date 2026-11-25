# mhwd-kernel

> مدیریت و نصب هسته‌های لینوکس در Manjaro.
> اطلاعات بیشتر: <https://wiki.manjaro.org/index.php/Manjaro_Kernels>.

- فهرست کردن همهٔ هسته‌های موجود:

`mhwd-kernel {{[-l|--list]}}`

- فهرست کردن همهٔ هسته‌های نصب‌شده:

`mhwd-kernel {{[-li|--listinstalled]}}`

- نصب هسته:

`sudo mhwd-kernel {{[-i|--install]}} {{kernel}}`

- حذف هسته:

`sudo mhwd-kernel {{[-r|--remove]}} {{kernel}}`

- نصب هسته و جایگزینی هستهٔ در حال اجرا:

`sudo mhwd-kernel {{[-i|--install]}} {{kernel}} rmc`
