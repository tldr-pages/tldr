# kdesrc-build

> ساخت آسان مؤلفه‌های KDE از مخازن کد منبع آن.
> اطلاعات بیشتر: <https://manned.org/kdesrc-build>.

- مقداردهی اولیهٔ `kdesrc-build`:

`kdesrc-build --initial-setup`

- کامپایل مؤلفهٔ KDE و وابستگی‌های آن از کد منبع:

`kdesrc-build {{component_name}}`

- کامپایل مؤلفه بدون به‌روزرسانی کد محلی و بدون کامپایل وابستگی‌های آن:

`kdesrc-build --no-src --no-include-dependencies {{component_name}}`

- تازه‌سازی دایرکتوری‌های ساخت پیش از کامپایل:

`kdesrc-build --refresh-build {{component_name}}`

- ادامهٔ کامپایل از وابستگی مشخص:

`kdesrc-build --resume-from {{dependency_component}} {{component_name}}`

- اجرای مؤلفه با نام فایل اجرایی مشخص:

`kdesrc-build --run --exec {{executable_name}} {{component_name}}`

- ساخت همهٔ مؤلفه‌های پیکربندی‌شده:

`kdesrc-build`

- استفاده از کتابخانه‌های سیستم به‌جای مؤلفه در صورت شکست ساخت:

`kdesrc-build --no-stop-on-failure {{component_name}}`
