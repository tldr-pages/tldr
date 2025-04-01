# restic

> 一个快速、安全的备份程序。
> 更多信息：<https://restic.net>.

- 在指定的本地目录中初始化备份仓库：

`restic init --repo {{path/to/repository}}`

- 将目录备份到仓库：

`restic --repo {{path/to/repository}} backup {{path/to/directory}}`

- 显示仓库中当前存储的备份快照：

`restic --repo {{path/to/repository}} snapshots`

- 将特定的备份快照恢复到目标目录：

`restic --repo {{path/to/repository}} restore {{latest|snapshot_id}} --target {{path/to/target}}`

- 从特定备份中恢复特定路径到目标目录：

`restic --repo {{path/to/repository}} restore {{snapshot_id}} --target {{path/to/target}} --include {{path/to/restore}}`

- 清理仓库，仅保留每个唯一备份的最新快照：

`restic forget --keep-last 1 --prune`
