# aws rds

> 使用 AWS Relational Database Service，一个用于设置、操作和扩展关系型数据库的 Web 服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/rds/>.

- 显示特定 RDS 子命令的帮助信息：

`aws rds {{子命令}} help`

- 停止实例：

`aws rds stop-db-instance --db-instance-identifier {{实例标识符}}`

- 启动实例：

`aws rds start-db-instance --db-instance-identifier {{实例标识符}}`

- 修改 RDS 实例：

`aws rds modify-db-instance --db-instance-identifier {{实例标识符}} {{参数}} --apply-immediately`

- 对 RDS 实例应用更新：

`aws rds apply-pending-maintenance-action --resource-identifier {{数据库_arn}} --apply-action {{系统更新}} --opt-in-type {{立即}}`

- 更改实例标识符：

`aws rds modify-db-instance --db-instance-identifier {{旧实例标识符}} --new-db-instance-identifier {{新实例标识符}}`

- 重启实例：

`aws rds reboot-db-instance --db-instance-identifier {{实例标识符}}`

- 删除实例：

`aws rds delete-db-instance --db-instance-identifier {{实例标识符}} --final-db-snapshot-identifier {{快照标识符}} --delete-automated-backups`
