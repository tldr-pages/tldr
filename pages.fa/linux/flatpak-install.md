# flatpak install

> نصب برنامه‌ها و محیط‌های اجرای Flatpak.
> همچنین ببینید: `flatpak`, `flatpak update`, `flatpak run`.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-install>.

- نصب یک برنامه از منبع راه دور:

`flatpak install {{remote_name}} {{com.example.app}}`

- نصب یک برنامه فقط برای کاربر فعلی:

`flatpak install {{[-u|--user]}} {{remote_name}} {{com.example.app}}`

- نصب یک شاخهٔ مشخص از برنامه:

`flatpak install {{remote_name}} {{com.example.app}}//{{branch}}`

- نصب یک برنامه از فایل یا URL با پسوند `.flatpakref`:

`flatpak install --from {{path/to/file.flatpakref|https://example.com/file.flatpakref}}`

- نصب یک برنامه از فایل بستهٔ `.flatpak`:

`flatpak install --bundle {{path/to/file.flatpak}}`

- نصب مجدد برنامه‌ای که قبلاً نصب شده است:

`flatpak install --reinstall {{remote_name}} {{com.example.app}}`

- به‌روزرسانی برنامه به جای هشدار در صورت نصب بودن آن:

`flatpak install --or-update {{remote_name}} {{com.example.app}}`

- نصب برنامه بدون درخواست تأیید:

`flatpak install {{[-y|--assumeyes]}} {{remote_name}} {{com.example.app}}`
