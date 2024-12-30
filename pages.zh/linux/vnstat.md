# vnstat

> 一个基于控制台的网络流量监控工具。
> 更多信息请访问：<https://manned.org/vnstat>。

- 显示所有接口的流量摘要：

`vnstat`

- 显示特定网络接口的流量摘要：

`vnstat -i {{network_interface}}`

- 显示特定网络接口的实时统计信息：

`vnstat -l -i {{network_interface}}`

- 使用条形图显示过去24小时按小时计算的流量统计：

`vnstat -hg`

- 测量并显示30秒的平均流量：

`vnstat -tr {{30}}`