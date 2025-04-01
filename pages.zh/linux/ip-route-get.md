# ip route get

> 获取到目标的单一路由，并以内核看到的方式精确打印其内容。
> 更多信息：<https://manned.org/ip-route>.

- 打印到目标的路由：

`ip {{[r|route]}} {{[g|get]}} {{1.1.1.1}}`

- 从特定源地址打印到目标的路由：

`ip {{[r|route]}} {{[g|get]}} {{destination}} from {{source}}`

- 打印从特定接口到达的包到目标的路由：

`ip {{[r|route]}} {{[g|get]}} {{destination}} iif {{eth0}}`

- 强制通过特定接口输出到目标的路由：

`ip {{[r|route]}} {{[g|get]}} {{destination}} oif {{eth1}}`

- 打印具有指定服务类型 (ToS) 到目标的路由：

`ip {{[r|route]}} {{[g|get]}} {{destination}} tos {{0x10}}`

- 使用特定的 VRF（虚拟路由和转发）实例打印到目标的路由：

`ip {{[r|route]}} {{[g|get]}} {{destination}} vrf {{myvrf}}`
