# autopkgtest

> اجرای آزمون‌ها روی بسته‌های دبیان.
> اطلاعات بیشتر: <https://manned.org/autopkgtest>.

- ساخت بسته در دایرکتوری فعلی و اجرای همهٔ آزمون‌ها مستقیماً روی سیستم:

`autopkgtest -- {{null}}`

- اجرای یک آزمون مشخص برای بستهٔ موجود در دایرکتوری فعلی:

`autopkgtest --test-name={{test_name}} -- {{null}}`

- دانلود و ساخت یک بستهٔ مشخص با `apt-get` و سپس اجرای همهٔ آزمون‌ها:

`autopkgtest {{package}} -- {{null}}`

- آزمودن بستهٔ موجود در دایرکتوری فعلی با استفاده از یک دایرکتوری ریشهٔ جدید:

`autopkgtest -- {{chroot}} {{path/to/new_root}}`

- آزمودن بستهٔ موجود در دایرکتوری فعلی بدون ساخت مجدد آن:

`autopkgtest {{[-B|--no-built-binaries]}} -- {{null}}`
