# vnstat

> 基于控制台的网络流量监控工具。
> 更多信息：<https://manned.org/vnstat>。

- 显示所有接口的流量摘要：

`vnstat`

- 显示特定网络接口的流量摘要：

`vnstat -i {{network_interface}}`

- 显示特定网络接口的实时统计信息：

`vnstat -l -i {{network_interface}}`

- 以柱状图形式显示过去24小时的每小时流量统计信息：

`vnstat -hg`

- 测量并显示30秒内的平均流量：

`vnstat -tr {{30}}`