# aws backup

> 用于保护 Amazon Web Services 服务及其关联数据的统一备份服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/backup/>.

- 返回指定 BackupPlanId 的备份计划详情：

`aws backup get-backup-plan --backup-plan-id {{标识符}}`

- 使用指定的备份计划名称和备份规则创建一个备份计划：

`aws backup create-backup-plan --backup-plan {{计划}}`

- 删除指定的备份计划：

`aws backup delete-backup-plan --backup-plan-id {{标识符}}`

- 列出当前账户的所有活动备份计划：

`aws backup list-backup-plans`

- 显示你的报告作业的详细信息：

`aws backup list-report-jobs`
