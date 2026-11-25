# kde-builder

> ساخت آسان مؤلفه‌های KDE از مخازن کد منبع آن.
> جایگزین سازگار با `kdesrc-build`.
> اطلاعات بیشتر: <https://kde-builder.kde.org/en/cmdline/supported-cmdline-params.html>.

- مقداردهی اولیهٔ `kde-builder`:

`kde-builder --initial-setup`

- کامپایل مؤلفهٔ KDE و وابستگی‌های آن از کد منبع (برای کامپایل دسکتاپ Plasma از `workspace` استفاده کنید):

`kde-builder {{component_name1 component_name2 ...}}`

- کامپایل مؤلفه بدون به‌روزرسانی کد محلی و بدون کامپایل وابستگی‌های آن:

`kde-builder {{[-SD|--no-src --no-include-dependencies]}} {{component_name}}`

- تازه‌سازی دایرکتوری‌های ساخت پیش از کامپایل:

`kde-builder {{[-r|--refresh-build]}} {{component_name}}`

- ادامهٔ کامپایل از وابستگی مشخص:

`kde-builder {{[-f|--resume-from]}} {{dependency_component}} {{component_name}}`

- اجرای مؤلفه با نام فایل اجرایی مشخص:

`kde-builder --run {{executable_name}}`

- نصب نشست ورود:

`kde-builder --install-login-session-only`

- استفاده از کتابخانه‌های سیستم به‌جای مؤلفه در صورت شکست ساخت:

`kde-builder --no-stop-on-failure {{component_name}}`
