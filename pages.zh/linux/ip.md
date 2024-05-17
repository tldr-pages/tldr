# ip

> 显示/操控路由、设备、路由规则和隧道。
> 某些子命令如 `ip address` 拥有自己的使用文档。
> 更多信息：<https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- 显示接口并带详细信息：

`ip address`

- 显示接口并带简要网络层信息：

`ip -brief address`

- 显示接口并带简要数据链路层信息：

`ip -brief link`

- 显示路由表：

`ip route`

- 显示邻居（ARP 表）：

`ip neighbour`

- 启用/禁用接口:

`ip link set {{接口}} {{up|down}}`
