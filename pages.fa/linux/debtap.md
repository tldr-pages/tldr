# debtap

> تبدیل بسته‌های دبیان به بسته‌های آرچ لینوکس.
> همچنین ببینید: `pacman-upgrade`.
> اطلاعات بیشتر: <https://github.com/helixarch/debtap#available-options>.

- به‌روزرسانی پایگاه دادهٔ debtap پیش از نخستین اجرا:

`sudo debtap {{[-u|--update]}}`

- تبدیل بستهٔ مشخص:

`debtap {{path/to/package.deb}}`

- تبدیل بستهٔ مشخص با گذشتن از همهٔ پرسش‌ها، به‌جز ویرایش فایل‌های فراداده:

`debtap {{[-q|--quiet]}} {{path/to/package.deb}}`

- تولید یک فایل PKGBUILD:

`debtap {{[-p|--pkgbuild]}} {{path/to/package.deb}}`
