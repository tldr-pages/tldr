# ip

> 显示/操作路由、设备、策略路由和隧道。
> 一些子命令如 `address` 有它们自己的使用文档。
> 更多信息：<https://www.manned.org/ip.8>。

- 列出带详细信息的接口：

`ip address`

- 列出带简要网络层信息的接口：

`ip -brief address`

- 列出带简要链路层信息的接口：

`ip -brief link`

- 显示路由表：

`ip route`

- 显示邻居（ARP 表）：

`ip neighbour`

- 将接口设置为启用/禁用：

`ip link set {{interface}} {{up|down}}`

- 向接口添加/删除 IP 地址：

`ip addr add/del {{ip}}/{{mask}} dev {{interface}}`

- 添加默认路由：

`ip route add default via {{ip}} dev {{interface}}`