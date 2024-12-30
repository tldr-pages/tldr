# tracert

> 接收有关您的计算机与目标之间路由每一步的信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>。

- 路由跟踪：

`tracert {{IP}}`

- 防止 `tracert` 将 IP 地址解析为主机名：

`tracert /d {{IP}}`

- 强制 `tracert` 仅使用 IPv4：

`tracert /4 {{IP}}`

- 强制 `tracert` 仅使用 IPv6：

`tracert /6 {{IP}}`

- 指定搜索目标的最大跳数：

`tracert /h {{max_hops}} {{IP}}`

- 显示帮助信息：

`tracert /?`