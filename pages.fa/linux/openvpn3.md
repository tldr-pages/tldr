# openvpn3

> کارخواه OpenVPN 3 برای لینوکس.
> اطلاعات بیشتر: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- شروع نشست جدید VPN:

`openvpn3 session-start {{[-c|--config]}} {{path/to/config.conf}}`

- فهرست کردن نشست‌های برقرارشده:

`openvpn3 sessions-list`

- قطع نشست برقرارشدهٔ فعلی که با پیکربندی مشخص شروع شده است:

`openvpn3 session-manage {{[-c|--config]}} {{path/to/config.conf}} {{[-D|--disconnect]}}`

- وارد کردن پیکربندی VPN:

`openvpn3 config-import {{[-c|--config]}} {{path/to/config.conf}}`

- فهرست کردن پیکربندی‌های واردشده:

`openvpn3 configs-list`
