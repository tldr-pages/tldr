# ip 邻居

> 邻居/ARP 表管理 IP 子命令。
> 更多信息：<https://manned.org/ip-neighbour.8>。

- 显示邻居/ARP 表条目：

`ip neighbour`

- 删除设备 `eth0` 上的邻居表条目：

`sudo ip neighbour flush dev {{eth0}}`

- 执行邻居查找并返回邻居条目：

`ip neighbour get {{lookup_ip}} dev {{eth0}}`

- 为邻居 IP 地址添加或删除 `eth0` 的 ARP 条目：

`sudo ip neighbour {{add|del}} {{ip_address}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- 更改或替换邻居 IP 地址到 `eth0` 的 ARP 条目：

`sudo ip neighbour {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{eth0}}`