# flatpak run

> اجرای برنامه‌ها و محیط‌های اجرای Flatpak.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- اجرای یک برنامهٔ نصب‌شده:

`flatpak run {{com.example.app}}`

- اجرای برنامهٔ نصب‌شده از شاخهٔ مشخص مانند stable، beta یا master:

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- اجرای پوستهٔ تعاملی درون Flatpak:

`flatpak run --command={{sh}} {{com.example.app}}`

- اجرای برنامهٔ نصب‌شده با نسخهٔ مشخص محیط اجرا:

`flatpak run --runtime-version={{24.08|master|stable|...}} {{com.example.app}}`

- اجرای برنامهٔ نصب‌شده با محیط اجرای متفاوت اما شمارهٔ نسخهٔ یکسان:

`flatpak run --runtime={{org.freedesktop.Sdk}} {{com.example.app}}`
