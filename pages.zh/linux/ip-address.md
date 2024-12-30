# IP 地址

> IP 地址管理子命令。
> 更多信息：<https://manned.org/ip-address>。

- 列出网络接口及其关联的 IP 地址：

`ip address`

- 过滤以仅显示活动网络接口：

`ip address show up`

- 显示特定网络接口的信息：

`ip address show dev {{eth0}}`

- 向网络接口添加 IP 地址：

`ip address add {{ip_address}} dev {{eth0}}`

- 从网络接口中删除 IP 地址：

`ip address delete {{ip_address}} dev {{eth0}}`

- 从网络接口中删除给定范围内的所有 IP 地址：

`ip address flush dev {{eth0}} scope {{global|host|link}}`