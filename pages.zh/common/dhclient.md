# dhclient

> DHCP 客户端。
> 更多信息：<https://manned.org/dhclient>。

- 获取 `eth0` 接口的 IP 地址：

`sudo dhclient {{eth0}}`

- 释放 `eth0` 接口的 IP 地址：

`sudo dhclient -r {{eth0}}`