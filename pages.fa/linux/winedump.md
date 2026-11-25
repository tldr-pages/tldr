# winedump

> چاپ محتوای فایل‌های دودویی Windows (مانند PE و NE)، رمزگشایی نام نمادهای C++ و تولید فایل‌های `.spec` برای Wine.
> اطلاعات بیشتر: <https://manned.org/winedump>.

- چاپ محتوای فایل PE، DLL یا اجرایی:

`winedump dump {{path/to/file.dll}}`

- چاپ فقط اطلاعات سربرگ فایل:

`winedump dump -f {{path/to/file.dll}}`

- چاپ بخش مشخص، مانند جدول واردات یا صادرات:

`winedump dump -j {{import|export}} {{path/to/file.dll}}`

- رمزگشایی نام نماد C++ تغییرنام‌یافته با MSVC:

`winedump sym {{mangled_symbol}}`

- تولید فایل `.spec` و کد پیاده‌سازی صوری از DLL:

`winedump spec {{path/to/file.dll}}`

- نمایش راهنما:

`winedump -h`
