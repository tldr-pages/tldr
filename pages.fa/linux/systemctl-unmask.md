# systemctl unmask

> برداشتن ماسک واحدها برای قابل شروع شدن دوباره.
> این کار اثر `systemctl mask` را برمی‌گرداند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#unmask%20UNIT%E2%80%A6>.

- برداشتن ماسک سرویس:

`systemctl unmask {{service_name}}`

- برداشتن ماسک و شروع فوری سرویس:

`systemctl unmask {{service_name}} --now`

- برداشتن ماسک سرویس کاربر:

`systemctl unmask {{service_name}} --user`
