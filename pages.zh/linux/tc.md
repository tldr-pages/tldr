# tc

> 显示/操作流量控制设置。
> 更多信息：<https://manned.org/tc>。

- 为出站数据包添加固定网络延迟：

`tc qdisc add dev {{eth0}} root netem delay {{delay_in_milliseconds}}ms`

- 为出站数据包添加正态分布的网络延迟：

`tc qdisc add dev {{eth0}} root netem delay {{mean_delay_ms}}ms {{delay_std_ms}}ms`

- 为部分数据包添加数据包损坏/丢失/重复：

`tc qdisc add dev {{eth0}} root netem {{corruption|loss|duplication}} {{effect_percentage}}%`

- 限制带宽、突发速率和最大延迟：

`tc qdisc add dev eth0 root tbf rate {{max_bandwidth_mb}}mbit burst {{max_burst_rate_kb}}kbit latency {{max_latency_before_drop_ms}}ms`

- 显示活动的流量控制策略：

`tc qdisc show dev {{eth0}}`

- 删除所有流量控制规则：

`tc qdisc del dev {{eth0}}`

- 更改流量控制规则：

`tc qdisc change dev {{eth0}} root netem {{policy}} {{policy_parameters}}`