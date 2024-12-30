# conntrack

> 与 Netfilter 连接追踪系统交互。
> 搜索、列出、检查、修改和删除连接流。
> 更多信息：<https://manned.org/conntrack>。

- 列出所有当前被追踪的连接：

`conntrack --dump`

- 显示连接变化的实时事件日志：

`conntrack --event`

- 显示连接变化及其相关时间戳的实时事件日志：

`conntrack --event -o timestamp`

- 显示特定 IP 地址的连接变化实时事件日志：

`conntrack --event --orig-src {{ip_address}}`

- 删除特定源 IP 地址的所有流：

`conntrack --delete --orig-src {{ip_address}}`