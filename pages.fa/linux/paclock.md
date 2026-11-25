# paclock

> قفل یا باز کردن قفل پایگاه دادهٔ libalpm (استفاده‌شده توسط `pacman`) برای جلوگیری یا اجازهٔ عملیات هم‌زمان مدیریت بسته.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/paclock.pod>.

- قفل کردن پایگاه داده:

`sudo paclock`

- نوشتن مسیر فایل قفل در `stdout` (بدون قفل کردن پایگاه داده):

`paclock --print`

- باز کردن قفل پایگاه داده:

`sudo paclock --unlock`

- نمایش راهنما:

`paclock --help`

- نمایش نسخه:

`paclock --version`
