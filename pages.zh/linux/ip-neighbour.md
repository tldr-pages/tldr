# ip neighbour

> 邻居/ARP 表管理 IP 子命令。
> 更多信息：<https://manned.org/ip-neighbour.8>。

- 显示邻居/ARP 表中的条目：

`ip {{[n|neighbour]}}`

- 从设备 `eth0` 上移除邻居表中的条目：

`sudo ip {{[n|neighbour]}} {{[f|flush]}} dev {{eth0}}`

- 执行邻居查找并返回邻居条目：

`ip {{[n|neighbour]}} {{[g|get]}} {{lookup_ip}} dev {{eth0}}`

- 为邻居 IP 地址添加或删除 ARP 条目，指定设备为 `eth0`：

`sudo ip {{[n|neighbour]}} {{add|delete}} {{ip_address}} lladdr {{mac_address}} dev {{eth0}} nud reachable`

- 更改或替换邻居 IP 地址在 `eth0` 上的 ARP 条目：

`sudo ip {{[n|neighbour]}} {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{eth0}}`
