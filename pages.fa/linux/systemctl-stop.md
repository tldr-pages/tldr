# systemctl stop

> توقف واحدهای systemd.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#stop%20PATTERN%E2%80%A6>.

- توقف واحد:

`systemctl stop {{unit}}`

- توقف سرویس و عدم نمایش هشدارها:

`systemctl stop {{unit}} --no-warn`

- توقف واحد کاربر:

`systemctl stop {{unit}} --user`
