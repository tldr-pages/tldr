# aws cloudwatch

> 监控 AWS 资源，以获得系统范围内的资源利用率、应用程序性能和运营健康状况的可见性。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html>.

- 列出账户的仪表板：

`aws cloudwatch list-dashboards`

- 显示指定仪表板的详细信息：

`aws cloudwatch get-dashboard --dashboard-name {{dashboard_name}}`

- 列出指标：

`aws cloudwatch list-metrics`

- 列出警报：

`aws cloudwatch describe-alarms`

- 创建或更新警报并将其与指标关联：

`aws cloudwatch put-metric-alarm --alarm-name {{alarm_name}} --evaluation-periods {{evaluation_periods}} --comparison-operator {{comparison_operator}}`

- 删除指定的警报：

`aws cloudwatch delete-alarms --alarm_names {{alarm_names}}`

- 删除指定的仪表板：

`aws cloudwatch delete-dashboards --dashboard-names {{dashboard_names}}`
