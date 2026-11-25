# fakeroot

> اجرای یک دستور در محیطی با دسترسی ساختگی ریشه برای تغییر فایل‌ها.
> اطلاعات بیشتر: <https://manned.org/fakeroot>.

- شروع پوستهٔ پیش‌فرض به‌صورت fakeroot:

`fakeroot`

- اجرای یک دستور به‌صورت fakeroot:

`fakeroot -- {{command}} {{command_arguments}}`

- اجرای یک دستور به‌صورت fakeroot و ذخیرهٔ محیط در فایل هنگام خروج با `-s`:

`fakeroot -s {{path/to/file}} -- {{command}} {{command_arguments}}`

- بارگذاری محیط fakeroot و اجرای یک دستور به‌صورت fakeroot:

`fakeroot -i {{path/to/file}} -- {{command}} {{command_arguments}}`

- اجرای یک دستور با حفظ مالکیت واقعی فایل‌ها به جای وانمود کردن به مالکیت ریشه:

`fakeroot {{[-u|--unknown-is-real]}} -- {{command}} {{command_arguments}}`

- نمایش راهنما:

`fakeroot {{[-h|--help]}}`
