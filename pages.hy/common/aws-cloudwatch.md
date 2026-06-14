# aws ամպային ժամացույց

> Վերահսկեք AWS ռեսուրսները՝ ռեսուրսների օգտագործման, հավելվածի կատարողականի և գործառնական առողջության տեսանելիություն ձեռք բերելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/>:.

- Ցուցակեք վահանակները ձեր հաշվի համար.:

`aws cloudwatch list-dashboards`

- Ցուցադրել մանրամասները նշված վահանակի համար.:

`aws cloudwatch get-dashboard --dashboard-name {{dashboard_name}}`

- Ցանկի չափումներ.:

`aws cloudwatch list-metrics`

- Ցուցակ ահազանգեր.:

`aws cloudwatch describe-alarms`

- Ստեղծեք կամ թարմացրեք ահազանգ և կապեք այն չափման հետ.:

`aws cloudwatch put-metric-alarm --alarm-name {{alarm_name}} --evaluation-periods {{evaluation_periods}} --comparison-operator {{comparison_operator}}`

- Ջնջել նշված ահազանգերը.:

`aws cloudwatch delete-alarms --alarm-names {{alarm_names}}`

- Ջնջել նշված վահանակները.:

`aws cloudwatch delete-dashboards --dashboard-names {{dashboard_names}}`
