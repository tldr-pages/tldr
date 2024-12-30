# velero

> 备份和迁移 Kubernetes 应用及其持久卷。
> 更多信息：<https://github.com/heptio/velero>。

- 创建一个包含所有资源的备份：

`velero backup create {{backup_name}}`

- 列出所有备份：

`velero backup get`

- 删除一个备份：

`velero backup delete {{backup_name}}`

- 创建一个每周备份，保留 90 天（2160 小时）：

`velero schedule create {{schedule_name}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}`

- 从最新的成功备份中创建恢复，触发特定的计划：

`velero restore create --from-schedule {{schedule_name}}`