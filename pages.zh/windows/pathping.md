# pathping

> 一种结合了 `ping` 和 `tracert` 功能的跟踪路由工具。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/pathping>。

- Ping 并跟踪到主机的路由：

`pathping {{hostname}}`

- 不进行 IP 地址到主机名的反向查找：

`pathping {{hostname}} -n`

- 指定搜索目标的最大跳数（默认是 30）：

`pathping {{hostname}} -h {{max_hops}}`

- 指定每次 ping 之间等待的毫秒数（默认是 240）：

`pathping {{hostname}} -p {{time}}`

- 指定每跳的查询次数（默认是 100）：

`pathping {{hostname}} -q {{queries}}`

- 强制使用 IPV4：

`pathping {{hostname}} -4`

- 强制使用 IPV6：

`pathping {{hostname}} -6`

- 显示帮助：

`pathping /?`