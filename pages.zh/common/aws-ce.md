# aws ce

> 通过 AWS Cost Explorer 服务运行成本管理操作。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html>.

- 创建异常监控：

`aws ce create-anomaly-monitor --monitor {{monitor_name}} --monitor-type {{monitor_type}}`

- 创建异常订阅：

`aws ce create-anomaly-subscription --subscription {{subscription_name}} --monitor-arn {{monitor_arn}} --subscribers {{subscribers}}`

- 获取异常：

`aws ce get-anomalies --monitor-arn {{monitor_arn}} --start-time {{start_time}} --end-time {{end_time}}`

- 获取成本和使用情况：

`aws ce get-cost-and-usage --time-period {{start_date}}/{{end_date}} --granularity {{granularity}} --metrics {{metrics}}`

- 获取成本预测：

`aws ce get-cost-forecast --time-period {{start_date}}/{{end_date}} --granularity {{granularity}} --metric {{metric}}`

- 获取预留实例利用率：

`aws ce get-reservation-utilization --time-period {{start_date}}/{{end_date}} --granularity {{granularity}}`

- 列出成本类别定义：

`aws ce list-cost-category-definitions`

- 标记资源：

`aws ce tag-resource --resource-arn {{resource_arn}} --tags {{tags}}`
