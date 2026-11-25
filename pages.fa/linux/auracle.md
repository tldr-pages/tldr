# auracle

> تعامل با مخزن کاربران آرچ لینوکس که معمولاً AUR نامیده می‌شود.
> اطلاعات بیشتر: <https://github.com/falconindy/auracle/blob/master/man/auracle.1.pod>.

- نمایش بسته‌های AUR مطابق با عبارت منظم `regex`:

`auracle search '{{regex}}'`

- نمایش اطلاعات یک یا چند بستهٔ AUR:

`auracle info {{package1 package2 ...}}`

- نمایش فایل `PKGBUILD` (اطلاعات ساخت) برای یک یا چند بستهٔ AUR:

`auracle show {{package1 package2 ...}}`

- نمایش به‌روزرسانی‌های بسته‌های نصب‌شدهٔ AUR:

`auracle outdated`
