# ip address

> IP 地址管理子命令。
> 更多信息：<https://manned.org/ip-address>。

- 列出网络接口及其关联的 IP 地址：

`ip {{[a|address]}}`

- 只显示活跃的网络接口：

`ip {{[a|address]}} {{[s|show]}} up`

- 显示特定网络接口的信息：

`ip {{[a|address]}} {{[s|show]}} {{eth0}}`

- 为网络接口添加 IP 地址：

`sudo ip {{[a|address]}} {{[a|add]}} {{ip_address}} dev {{eth0}}`

- 从网络接口删除 IP 地址：

`sudo ip {{[a|address]}} {{[d|delete]}} {{ip_address}} dev {{eth0}}`

- 从网络接口删除指定范围内的所有 IP 地址：

`sudo ip {{[a|address]}} {{[f|flush]}} {{eth0}} scope {{global|host|link}}`
