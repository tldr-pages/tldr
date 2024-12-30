# vnstati

> vnStat 的 PNG 图像输出支持。
> 更多信息：<https://manned.org/vnstati>。

- 输出最近 2 个月、天数和所有时间的摘要：

`vnstati --summary --iface {{network_interface}} --output {{path/to/output.png}}`

- 输出所有时间中流量最密集的 10 天：

`vnstati --top 10 --iface {{network_interface}} --output {{path/to/output.png}}`

- 输出过去 12 个月的每月流量统计：

`vnstati --months --iface {{network_interface}} --output {{path/to/output.png}}`

- 输出过去 24 小时的每小时流量统计：

`vnstati --hours --iface {{network_interface}} --output {{path/to/output.png}}`