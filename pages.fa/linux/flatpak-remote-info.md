# flatpak remote-info

> نمایش اطلاعات یک برنامه یا محیط اجرا در منبع راه دور.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-info>.

- نمایش اطلاعات یک Flatpak:

`flatpak remote-info {{remote_name}} {{com.example.app}}`

- نمایش گزارش نسخه‌های قبلی در منبع راه دور:

`flatpak remote-info --log {{remote_name}} {{com.example.app}}`

- نمایش اطلاعات کامیت مشخص به جای آخرین نسخه:

`flatpak remote-info --commit {{COMMIT}} {{remote_name}} {{com.example.app}}`
