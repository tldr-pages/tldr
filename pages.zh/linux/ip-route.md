# ip route

> IP 路由表管理子命令。
> 更多信息：<https://manned.org/ip-route>。

- 显示 `main` 路由表：

`ip {{[r|route]}}`

- 使用网关转发添加默认路由：

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- 使用 `eth0` 添加默认路由：

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{eth0}}`

- 添加静态路由：

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- 删除静态路由：

`sudo ip {{[r|route]}} {{[d|delete]}} {{destination_ip}} dev {{eth0}}`

- 更改或替换静态路由：

`sudo ip {{[r|route]}} {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- 显示内核将使用哪个路由来访问 IP 地址：

`ip {{[r|route]}} {{[g|get]}} {{destination_ip}}`

- 显示特定的路由表：

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{table_number}}`
