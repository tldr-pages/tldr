# systemctl add-wants

> افزودن وابستگی‌های `Wants` به یک هدف برای یک یا چند واحد.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#add-wants%20TARGET%20UNIT%E2%80%A6>.

- افزودن وابستگی `Wants` از هدف به واحد:

`systemctl add-wants {{target}} {{unit}}`

- افزودن چند وابستگی `Wants` هم‌زمان:

`systemctl add-wants {{target}} {{unit1 unit2 ...}}`

- افزودن وابستگی `Wants` در سطح کاربر:

`systemctl add-wants {{target}} {{unit}} --user`
