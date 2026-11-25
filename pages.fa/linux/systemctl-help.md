# systemctl help

> نمایش صفحات راهنمای یک یا چند واحد یا واحد متعلق به فرایند با PID.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#help%20PATTERN%E2%80%A6%7CPID%E2%80%A6>.

- نمایش صفحهٔ راهنمای واحد مشخص:

`systemctl help {{unit}}`

- نمایش صفحات راهنمای چند واحد:

`systemctl help {{unit1 unit2 ...}}`

- نمایش صفحهٔ راهنمای واحد کاربر:

`systemctl help {{unit}} --user`

- نمایش صفحهٔ راهنما بدون صفحه‌بند (همه در یک بار):

`systemctl help {{unit}} --no-pager`

- نمایش صفحهٔ راهنمای واحد فرایند با PID:

`systemctl help {{process_id}}`
