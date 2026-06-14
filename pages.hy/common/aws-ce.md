# aws ce

> Գործարկել ծախսերի կառավարման գործառնությունները AWS Cost Explorer ծառայության միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/ce/>:.

- Ստեղծեք անոմալիաների մոնիտոր.:

`aws ce create-anomaly-monitor --monitor {{monitor_name}} --monitor-type {{monitor_type}}`

- Ստեղծեք անոմալի բաժանորդագրություն.:

`aws ce create-anomaly-subscription --subscription {{subscription_name}} --monitor-arn {{monitor_arn}} --subscribers {{subscribers}}`

- Ստացեք անոմալիաներ.:

`aws ce get-anomalies --monitor-arn {{monitor_arn}} --start-time {{start_time}} --end-time {{end_time}}`

- Ստացեք արժեքը և օգտագործումը.:

`aws ce get-cost-and-usage --time-period {{start_date}}/{{end_date}} --granularity {{granularity}} --metrics {{metrics}}`

- Ստացեք ծախսերի կանխատեսում.:

`aws ce get-cost-forecast --time-period {{start_date}}/{{end_date}} --granularity {{granularity}} --metric {{metric}}`

- Ստացեք ամրագրման օգտագործումը.:

`aws ce get-reservation-utilization --time-period {{start_date}}/{{end_date}} --granularity {{granularity}}`

- Թվարկեք ծախսերի կատեգորիայի սահմանումները.:

`aws ce list-cost-category-definitions`

- Tag ռեսուրս:

`aws ce tag-resource --resource-arn {{resource_arn}} --tags {{tags}}`
