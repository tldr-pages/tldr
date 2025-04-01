# aws backup

> 统一备份服务，旨在保护 Amazon Web Services 服务及其关联的数据。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- 获取特定 BackupPlanId 的备份计划详细信息：

`aws backup get-backup-plan --backup-plan-id {{id}}`

- 使用特定的备份计划名称和备份规则创建备份计划：

`aws backup create-backup-plan --backup-plan {{plan}}`

- 删除特定的备份计划：

`aws backup delete-backup-plan --backup-plan-id {{id}}`

- 列出当前账户的所有活动备份计划：

`aws backup list-backup-plans`

- 显示有关报告作业的详细信息：

`aws backup list-report-jobs`