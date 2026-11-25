# flatpak search

> جست‌وجوی برنامه‌ها و محیط‌های اجرای Flatpak در منابع راه دور پیکربندی‌شده.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-search>.

- جست‌وجوی یک برنامه یا محیط اجرا:

`flatpak search "{{text}}"`

- جست‌وجو فقط در منابع راه دور کاربر فعلی:

`flatpak search {{[-u|--user]}} "{{text}}"`

- نمایش ستون‌های مشخص برای هر نتیجه:

`flatpak search --columns {{name,application,version,...}} "{{text}}"`
