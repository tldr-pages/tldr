# aws logs

> Interact with log files from various AWS services.
> More information: <https://docs.aws.amazon.com/cli/latest/reference/logs/>.

- List log groups:

`aws logs list-log-groups`

- Continuously poll logs of a CloudWatch log group:

`aws logs tail {{log_group_name}} --follow`

- Tail the logs of a CloudWatch log group based on a filter:

`aws logs tail {{log_group_name}} --filter-pattern {{pattern}}`

- Stream near real-time logs from a log group:

`aws logs start-live-tail --log-group-identifiers {{log_group_name}}`

- Export logs to an S3 bucket:

`aws logs create-export-task --log-group-name {{log_group_name}} --from {{start_time}} --to {{end_time}} --destination {{s3_bucket_name}}`
