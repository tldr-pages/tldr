# ip route

> IP 路由表管理子命令。
> 更多信息: <https://manned.org/ip-route>。

- 显示路由表：

`ip route {{show|list}}`

- 使用网关转发添加默认路由：

`sudo ip route add default via {{gateway_ip}}`

- 使用 `eth0` 添加默认路由：

`sudo ip route add default dev {{eth0}}`

- 添加静态路由：

`sudo ip route add {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- 删除静态路由：

`sudo ip route del {{destination_ip}} dev {{eth0}}`

- 更改或替换静态路由：

`sudo ip route {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- 显示内核将使用哪个路由到达一个 IP 地址：

`ip route get {{destination_ip}}`