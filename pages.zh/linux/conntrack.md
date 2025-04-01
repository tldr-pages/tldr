# conntrack

> 与 Netfilter 连接跟踪系统进行交互。
> 搜索、列出、检查、修改和删除连接流。
> 更多信息：<https://manned.org/conntrack>.

- 列出所有当前被跟踪的连接：

`conntrack --dump`

- 显示连接变化的实时事件日志：

`conntrack --event`

- 显示连接变化的实时事件日志并附带时间戳：

`conntrack --event -o timestamp`

- 显示特定 IP 地址的连接变化的实时事件日志：

`conntrack --event --orig-src {{ip_address}}`

- 删除特定源 IP 地址的所有连接流：

`conntrack --delete --orig-src {{ip_address}}`
