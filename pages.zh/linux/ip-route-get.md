# ip route get

> 获取到达目标的单一路由，并完全按照内核的视角打印其内容。
> 更多信息：<https://manned.org/ip-route>。

- 打印到目标的路由：

`ip route get {{1.1.1.1}}`

- 从特定源地址打印到目标的路由：

`ip route get {{destination}} from {{source}}`

- 打印到目标的路由，对于在特定接口上到达的数据包：

`ip route get {{destination}} iif {{eth0}}`

- 打印到目标的路由，强制输出通过特定接口：

`ip route get {{destination}} oif {{eth1}}`

- 打印到目标的路由，带有指定的服务类型（ToS）：

`ip route get {{destination}} tos {{0x10}}`

- 使用特定的虚拟路由和转发（VRF）实例打印到目标的路由：

`ip route get {{destination}} vrf {{myvrf}}`