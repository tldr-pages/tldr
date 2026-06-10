# aws տեղեկամատյան

> Փոխազդեք AWS տարբեր ծառայությունների մատյան ֆայլերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/logs/>:.

- Ցուցակ մատյան խմբեր.:

`aws logs list-log-groups`

- CloudWatch տեղեկամատյանների խմբի շարունակական հարցումների տեղեկամատյանները.:

`aws logs tail {{log_group_name}} --follow`

- Զտեք CloudWatch տեղեկամատյանների խմբի տեղեկամատյանները՝ հիմնված ֆիլտրի վրա.:

`aws logs tail {{log_group_name}} --filter-pattern {{pattern}}`

- Հեռարձակեք իրական ժամանակի տեղեկամատյանների մոտ տեղեկամատյանների խմբից.:

`aws logs start-live-tail --log-group-identifiers {{log_group_name}}`

- Արտահանել տեղեկամատյանները S3 դույլ.:

`aws logs create-export-task --log-group-name {{log_group_name}} --from {{start_time}} --to {{end_time}} --destination {{s3_bucket_name}}`
