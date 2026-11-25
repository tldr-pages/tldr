# systemctl is-active

> بررسی فعال بودن یک یا چند واحد systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#is-active%20PATTERN%E2%80%A6>.

- بررسی فعال بودن واحد:

`systemctl is-active {{unit}}`

- بررسی فعال بودن چند واحد:

`systemctl is-active {{unit1 unit2 ...}}`

- بررسی فعال بودن واحد بدون چاپ وضعیت در `stdout`:

`systemctl is-active {{unit}} {{[-q|--quiet]}}`

- بررسی فعال بودن واحد کاربر:

`systemctl is-active {{unit}} --user`
