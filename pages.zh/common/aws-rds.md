# AWS RDS

> 使用 AWS 关系数据库服务，这是一个设置、操作和扩展关系数据库的网络服务。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>。

- 显示特定 RDS 子命令的帮助：

`aws rds {{subcommand}} help`

- 停止实例：

`aws rds stop-db-instance --db-instance-identifier {{instance_identifier}}`

- 启动实例：

`aws rds start-db-instance --db-instance-identifier {{instance_identifier}}`

- 修改 RDS 实例：

`aws rds modify-db-instance --db-instance-identifier {{instance_identifier}} {{parameters}} --apply-immediately`

- 对 RDS 实例应用更新：

`aws rds apply-pending-maintenance-action --resource-identifier {{database_arn}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- 更改实例标识符：

`aws rds modify-db-instance --db-instance-identifier {{old_instance_identifier}} --new-db-instance-identifier {{new_instance_identifier}}`

- 重启实例：

`aws rds reboot-db-instance --db-instance-identifier {{instance_identifier}}`

- 删除实例：

`aws rds delete-db-instance --db-instance-identifier {{instance_identifier}} --final-db-snapshot-identifier {{snapshot_identifier}} --delete-automated-backups`