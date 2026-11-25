# dpkg-buildpackage

> کامپایل بسته‌های دودویی و یا منبع دبیان از کد منبع.
> معمولاً در درخت منبعی اجرا می‌شود که دایرکتوری `debian/` دارد.
> وابستگی‌های ساخت را نیز مدیریت می‌کند، فایل‌هایی مانند `.buildinfo` و `.changes` می‌سازد و در صورت لزوم نتیجه را امضا می‌کند.
> اطلاعات بیشتر: <https://manned.org/dpkg-buildpackage>.

- تولید بسته‌های منبع و دودویی:

`dpkg-buildpackage`

- تولید فقط بسته‌های دودویی بدون بستهٔ منبع:

`dpkg-buildpackage {{[-b|--build=binary]}}`

- تولید فقط بستهٔ منبع بدون کامپایل فایل‌های دودویی:

`dpkg-buildpackage {{[-S|--build=source]}}`

- امضا نکردن فایل‌های `.dsc` و `.changes`:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- اجرا نکردن `clean` پیش از کامپایل:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- استفاده از `fakeroot` به‌عنوان دستور کسب دسترسی ریشه هنگام ساخت:

`dpkg-buildpackage {{[-r|--root-command=]}}fakeroot`

- اجرای یک هدف مشخص در `debian/rules`:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`
