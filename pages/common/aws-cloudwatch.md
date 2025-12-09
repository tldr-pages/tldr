# aws cloudwatch

> Monitor AWS resources to gain system-wide visibility into resource utilization, application performance, and operational health.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html>.

- List dashboards for your account:

`aws cloudwatch list-dashboards`

- Display details for the specified dashboard:

`aws cloudwatch get-dashboard --dashboard-name {{dashboard_name}}`

- List metrics:

`aws cloudwatch list-metrics`

- List alarms:

`aws cloudwatch describe-alarms`

- Create or update an alarm and associate it with a metric:

`aws cloudwatch put-metric-alarm --alarm-name {{alarm_name}} --evaluation-periods {{evaluation_periods}} --comparison-operator {{comparison_operator}}`

- Delete the specified alarms:

`aws cloudwatch delete-alarms --alarm_names {{alarm_names}}`

- Delete the specified dashboards:

`aws cloudwatch delete-dashboards --dashboard-names {{dashboard_names}}`
