# iwconfig

> 配置和显示无线网络接口的参数。
> 更多信息：<https://manned.org/iwconfig>。

- 显示所有接口的参数和统计信息：

`iwconfig`

- 显示指定接口的参数和统计信息：

`iwconfig {{interface}}`

- 设置指定接口的 ESSID（网络名称）（例如 eth0 或 wlp2s0）：

`iwconfig {{interface}} {{new_network_name}}`

- 设置指定接口的工作模式：

`iwconfig {{interface}} mode {{Ad-Hoc|Managed|Master|Repeater|Secondary|Monitor|Auto}}`