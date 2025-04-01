# ip route add

> 添加新的网络路由。
> 更多信息：<https://manned.org/ip-route>.

- 使用网关转发添加默认路由：

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- 使用 `eth0` 添加默认路由：

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{eth0}}`

- 添加静态路由：

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- 向特定路由表添加路由：

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} dev {{eth0}} {{[t|table]}} {{ip}}`