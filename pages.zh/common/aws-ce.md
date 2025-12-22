# aws ce

> 通过 AWS Cost Explorer 服务运行成本管理操作。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/ce/>.

- 创建异常监控器：

`aws ce create-anomaly-monitor --monitor {{监控器名称}} --monitor-type {{监控器类型}}`

- 创建异常订阅：

`aws ce create-anomaly-subscription --subscription {{订阅名称}} --monitor-arn {{监控器 ARN}} --subscribers {{订阅者}}`

- 获取异常信息：

`aws ce get-anomalies --monitor-arn {{监控器 ARN}} --start-time {{开始时间}} --end-time {{结束时间}}`

- 获取成本和使用情况：

`aws ce get-cost-and-usage --time-period {{开始日期}}/{{结束日期}} --granularity {{粒度}} --metrics {{指标}}`

- 获取成本预测：

`aws ce get-cost-forecast --time-period {{开始日期}}/{{结束日期}} --granularity {{粒度}} --metric {{指标}}`

- 获取预留实例使用率：

`aws ce get-reservation-utilization --time-period {{开始日期}}/{{结束日期}} --granularity {{粒度}}`

- 列出成本类别定义：

`aws ce list-cost-category-definitions`

- 为资源添加标签：

`aws ce tag-resource --resource-arn {{资源 ARN}} --tags {{标签}}`
