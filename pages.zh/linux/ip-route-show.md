# ip route show

> 显示 IP 路由表管理的子命令。
> 更多信息：<https://manned.org/ip-route>。

- 显示路由表：

`ip route show`

- 显示主路由表（与第一个示例相同）：

`ip route show {{main|254}}`

- 显示本地路由表：

`ip route show table {{local|255}}`

- 显示所有路由表：

`ip route show table {{all|unspec|0}}`

- 仅列出来自特定设备的路由：

`ip route show dev {{eth0}}`

- 列出特定范围内的路由：

`ip route show scope link`

- 显示路由缓存：

`ip route show cache`

- 仅显示 IPv6 或 IPv4 路由：

`ip {{-6|-4}} route show`