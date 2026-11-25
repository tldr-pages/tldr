# flatpak uninstall

> حذف برنامه‌ها و محیط‌های اجرای Flatpak.
> همچنین : `flatpak install`, `flatpak update`.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-uninstall>.

- حذف یک برنامه یا محیط اجرا:

`flatpak uninstall {{com.example.app}}`

- حذف برنامه از نصب مخصوص کاربر:

`flatpak uninstall {{[-u|--user]}} {{com.example.app}}`

- حذف برنامه و پاک کردن داده‌های آن در `~/.var/app`:

`flatpak uninstall --delete-data {{com.example.app}}`

- حذف همهٔ برنامه‌ها و محیط‌های اجرای استفاده‌نشده:

`flatpak uninstall --unused`

- حذف داده‌های همهٔ برنامه‌هایی که دیگر نصب نیستند:

`flatpak uninstall --delete-data`

- حذف برنامه بدون درخواست تأیید:

`flatpak uninstall {{[-y|--assumeyes]}} {{com.example.app}}`

- حذف همهٔ برنامه‌ها و محیط‌های اجرا:

`flatpak uninstall --all`
