# bmon

> 监控带宽并捕获网络相关统计信息。
> 更多信息：<https://manned.org/bmon>.

- 显示所有接口的列表：

`bmon -a`

- 以每秒位数显示数据传输速率：

`bmon -b`

- 设置策略以定义显示哪些网络接口：

`bmon -p {{interface_1,interface_2,interface_3}}`

- 设置计算每个计数器速率的间隔（以秒为单位）：

`bmon -R {{2.0}}`
