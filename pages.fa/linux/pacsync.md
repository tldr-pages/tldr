# pacsync

> به‌روزرسانی پایگاه‌های دادهٔ همگام‌سازی.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacsync.pod>.

- به‌روزرسانی همهٔ پایگاه‌های دادهٔ همگام‌سازی:

`sudo pacsync`

- به‌روزرسانی پایگاه‌های دادهٔ همگام‌سازی مشخص:

`sudo pacsync {{repository1 repository2 ...}}`

- به‌روزرسانی پایگاه‌های دادهٔ همگام‌سازی حتی اگر از قبل به‌روز باشند:

`sudo pacsync --force`

- به‌روزرسانی پایگاه‌های دادهٔ همگام‌سازی با فایل پیکربندی مشخص:

`sudo pacsync --config {{path/to/pacman.conf}}`

- به‌روزرسانی پایگاه‌های دادهٔ همگام‌سازی و بازگرداندن true فقط در صورت به‌روزرسانی واقعی یک پایگاه داده:

`sudo pacsync --updated`
