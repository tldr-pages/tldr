# nmcli connection

> 使用 NetworkManager 管理连接。
> 该子命令也可以用 `nmcli c` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 列出所有 NetworkManager 连接（显示名称、UUID、类型和设备）：

`nmcli connection`

- 激活一个连接：

`nmcli connection up uuid {{uuid}}`

- 停用一个连接：

`nmcli connection down uuid {{uuid}}`

- 创建一个自动配置的双栈连接：

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ipv4.method {{auto}} ipv6.method {{auto}}`

- 创建一个静态 IPv6 专用连接：

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip6 {{2001:db8::2/64}} gw6 {{2001:db8::1}} ipv6.dns {{2001:db8::1}} ipv4.method {{ignore}}`

- 创建一个静态 IPv4 专用连接：

`nmcli connection add ifname {{interface_name}} type {{ethernet}} ip4 {{10.0.0.7/8}} gw4 {{10.0.0.1}} ipv4.dns {{10.0.0.1}} ipv6.method {{ignore}}`

- 从 OVPN 文件创建一个使用 OpenVPN 的 VPN 连接：

`nmcli connection import type {{openvpn}} file {{path/to/vpn_config.ovpn}}`