# secret-tool

> ذخیره و بازیابی رمزهای عبور، بخشی از بستهٔ `libsecret`.
> با پیاده‌سازی‌های سرویس محرمانهٔ Freedesktop مانند `gnome-keyring` ارتباط برقرار می‌کند.
> اطلاعات بیشتر: <https://gnome.pages.gitlab.gnome.org/libsecret/>.

- ذخیرهٔ اطلاعات محرمانه با برچسب اختیاری:

`secret-tool store --label={{label}} {{key}} {{value}}`

- بازیابی اطلاعات محرمانه:

`secret-tool lookup key {{key}}`

- دریافت اطلاعات بیشتر دربارهٔ مورد محرمانه:

`secret-tool search key {{key}}`

- حذف اطلاعات محرمانهٔ ذخیره‌شده:

`secret-tool clear key {{key}}`
