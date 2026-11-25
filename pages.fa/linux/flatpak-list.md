# flatpak list

> فهرست کردن برنامه‌ها و محیط‌های اجرای نصب‌شدهٔ Flatpak.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-list>.

- فهرست کردن همهٔ برنامه‌ها و محیط‌های اجرای نصب‌شده:

`flatpak list`

- فهرست کردن فقط برنامه‌های نصب‌شده:

`flatpak list --app`

- فهرست کردن فقط محیط‌های اجرای نصب‌شده:

`flatpak list --runtime`

- فهرست کردن همهٔ محیط‌های اجرا، از جمله افزونه‌های زبان و اشکال‌زدایی:

`flatpak list {{[-a|--all]}}`

- فهرست کردن برنامه‌ها و محیط‌های اجرای نصب‌شده برای کاربر فعلی:

`flatpak list {{[-u|--user]}}`

- نمایش جزئیاتی مانند منشأ و اندازه:

`flatpak list {{[-d|--show-details]}}`
