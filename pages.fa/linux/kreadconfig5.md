# kreadconfig5

> خواندن ورودی‌های KConfig برای KDE Plasma.
> اطلاعات بیشتر: <https://userbase.kde.org/KDE_System_Administration/Configuration_Files>.

- خواندن کلید از پیکربندی سراسری:

`kreadconfig5 --group {{group_name}} --key {{key_name}}`

- خواندن کلید از فایل پیکربندی مشخص:

`kreadconfig5 --file {{path/to/file}} --group {{group_name}} --key {{key_name}}`

- بررسی استفاده از systemd برای شروع نشست Plasma:

`kreadconfig5 --file {{startkderc}} --group {{General}} --key systemdBoot`
