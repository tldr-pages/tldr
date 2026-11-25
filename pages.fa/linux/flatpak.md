# flatpak

> ساخت، نصب و اجرای برنامه‌ها و محیط‌های اجرای Flatpak.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- اجرای یک برنامهٔ نصب‌شده:

`flatpak run {{com.example.app}}`

- نصب یک برنامه از منبع راه دور:

`flatpak install {{remote_name}} {{com.example.app}}`

- فهرست کردن برنامه‌های نصب‌شده بدون محیط‌های اجرا:

`flatpak list --app`

- به‌روزرسانی همهٔ برنامه‌ها و محیط‌های اجرای نصب‌شده:

`flatpak update`

- افزودن یک منبع راه دور:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- حذف یک برنامهٔ نصب‌شده:

`flatpak remove {{com.example.app}}`

- حذف همهٔ برنامه‌های استفاده‌نشده:

`flatpak remove --unused`

- نمایش اطلاعات یک برنامهٔ نصب‌شده:

`flatpak info {{com.example.app}}`
