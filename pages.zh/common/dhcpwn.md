# dhcpwn

> 测试 DHCP IP 耗尽攻击并嗅探本地 DHCP 流量。
> 更多信息：<https://github.com/mschwager/dhcpwn>。

- 使用 IP 请求淹没网络：

`dhcpwn --interface {{network_interface}} flood --count {{number_of_requests}}`

- 嗅探本地 DHCP 流量：

`dhcpwn --interface {{network_interface}} sniff`