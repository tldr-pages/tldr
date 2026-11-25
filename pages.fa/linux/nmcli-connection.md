# nmcli connection

> مدیریت اتصال‌ها با NetworkManager.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#connection>.

- فهرست کردن همهٔ اتصال‌های NetworkManager (نمایش نام، UUID، نوع و دستگاه):

`nmcli {{[c|connection]}}`

- فعال کردن اتصال:

`nmcli {{[c|connection]}} {{[u|up]}} {{uuid}}`

- غیرفعال کردن اتصال:

`nmcli {{[c|connection]}} {{[d|down]}} {{uuid}}`

- ایجاد اتصال دوپشته با پیکربندی خودکار:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{interface_name}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- ایجاد اتصال ایستا فقط برای IPv6:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{interface_name}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- ایجاد اتصال ایستا فقط برای IPv4:

`nmcli {{[c|connection]}} {{[a|add]}} ifname {{interface_name}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- ایجاد اتصال VPN با OpenVPN از فایل OVPN:

`nmcli {{[c|connection]}} {{[i|import]}} type {{openvpn}} file {{path/to/vpn_config.ovpn}}`
