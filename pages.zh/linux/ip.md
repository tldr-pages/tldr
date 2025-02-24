# ip

> 显示/操作路由、设备、策略路由和隧道。
> 一些子命令（例如 `address`）有自己的使用文档。
> 更多信息：<https://www.manned.org/ip.8>.

- 列出带有详细信息的接口：

`ip {{[a|address]}}`

- 列出带有简要网络层信息的接口：

`ip {{[-br a|-brief address]}}`

- 列出带有简要链路层信息的接口：

`ip {{[-br l|-brief link]}}`

- 显示路由表：

`ip {{[r|route]}}`

- 显示邻居（ARP 表）：

`ip {{[n|neighbour]}}`

- 使接口启动/关闭：

`ip {{[l|link]}} set {{interface}} {{up|down}}`

- 向接口添加/删除 IP 地址：

`ip {{[a|address]}} add/del {{ip}}/{{mask}} dev {{interface}}`

- 添加默认路由：

`ip {{[r|route]}} add default via {{ip}} dev {{interface}}`
