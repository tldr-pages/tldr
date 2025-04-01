# velero

> 备份和迁移 Kubernetes 应用程序及其持久卷。
> 更多信息：<https://github.com/heptio/velero>.

- 创建包含所有资源的备份：

`velero backup create {{backup_name}}`

- 列出所有备份：

`velero backup get`

- 删除备份：

`velero backup delete {{backup_name}}`

- 创建每周一次的备份，每个备份保留 90 天（2160 小时）：

`velero schedule create {{schedule_name}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}`

- 从特定计划触发的最新成功备份中创建还原：

`velero restore create --from-schedule {{schedule_name}}`