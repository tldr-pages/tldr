# systemctl add-requires

> افزودن وابستگی‌های `Requires` به یک هدف برای یک یا چند واحد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#add-wants%20TARGET%20UNIT%E2%80%A6>.

- افزودن وابستگی `Requires` از هدف به واحد:

`systemctl add-requires {{target}} {{unit}}`

- افزودن چند وابستگی `Requires` هم‌زمان:

`systemctl add-requires {{target}} {{unit1 unit2 ...}}`

- افزودن وابستگی `Requires` در سطح کاربر:

`systemctl add-requires {{target}} {{unit}} --user`
