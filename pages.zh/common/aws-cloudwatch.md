# aws cloudwatch

> 监控 AWS 资源，以获得对资源利用率、应用程序性能和运行状况的全局可见性。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/>.

- 列出你账户中的仪表板：

`aws cloudwatch list-dashboards`

- 显示指定仪表板的详细信息：

`aws cloudwatch get-dashboard --dashboard-name {{仪表板名称}}`

- 列出指标：

`aws cloudwatch list-metrics`

- 列出告警：

`aws cloudwatch describe-alarms`

- 创建或更新一个告警，并将其与某个指标关联：

`aws cloudwatch put-metric-alarm --alarm-name {{告警名称}} --evaluation-periods {{评估周期数}} --comparison-operator {{比较运算符}}`

- 删除指定的告警：

`aws cloudwatch delete-alarms --alarm_names {{告警名称列表}}`

- 删除指定的仪表板：

`aws cloudwatch delete-dashboards --dashboard-names {{仪表板名称列表}}`
