# avahi-resolve

> 在主机名和 IP 地址之间进行转换。
> 更多信息：<https://www.avahi.org/>.

- 将本地服务解析为 IPv4 地址：

`avahi-resolve -4 {{[-n|--name]}} {{service.local}}`

- 详细地将 IP 地址解析为主机名：

`avahi-resolve {{[-v|--verbose]}} {{[-a|--address]}} {{IP}}`