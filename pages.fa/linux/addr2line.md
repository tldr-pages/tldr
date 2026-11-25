# addr2line

> تبدیل آدرس‌های یک فایل دودویی به نام فایل‌ها و شمارهٔ خط‌ها.
> اطلاعات بیشتر: <https://manned.org/addr2line>.

- نمایش نام فایل و شمارهٔ خط کد منبع از روی آدرس یک دستور در فایل اجرایی:

`addr2line {{[-e|--exe]}} {{path/to/executable}} {{address}}`

- نمایش نام تابع، نام فایل و شمارهٔ خط:

`addr2line {{[-e|--exe]}} {{path/to/executable}} {{[-f|--functions]}} {{address}}`

- بازگرداندن نام تابع تغییرشکل‌یافته در کد C++ به شکل خوانا:

`addr2line {{[-e|--exe]}} {{path/to/executable}} {{[-f|--functions]}} {{[-C|--demangle]}} {{address}}`
