# makepkg

> ایجاد بستهٔ قابل استفاده با `pacman`.
> به‌طور پیش‌فرض از فایل `PKGBUILD` در دایرکتوری کاری فعلی استفاده می‌کند.
> اطلاعات بیشتر: <https://manned.org/makepkg>.

- ساخت بسته:

`makepkg`

- ساخت بسته و نصب وابستگی‌های آن:

`makepkg {{[-s|--syncdeps]}}`

- ساخت بسته، نصب وابستگی‌ها و سپس نصب آن در سیستم:

`makepkg {{[-si|--syncdeps --install]}}`

- ساخت بسته بدون بررسی هش منابع، امضاهای PGP و تابع `check()` در `PKGBUILD`:

`makepkg --skipchecksums --skippgpcheck --nocheck`

- پاک‌سازی دایرکتوری‌های کاری پس از ساخت موفق:

`makepkg {{[-c|--clean]}}`

- بررسی هش منابع:

`makepkg --verifysource`

- تولید و ذخیرهٔ اطلاعات منبع در `.SRCINFO`:

`makepkg --printsrcinfo >.SRCINFO`

- بارگیری منبع و نصب فقط وابستگی‌های ساخت برنامه:

`makepkg {{[-so|--syncdeps --nobuild]}}`
