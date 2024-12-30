# restic

> 一款快速、安全的备份程序。
> 更多信息：<https://restic.net>。

- 在指定的本地目录中初始化备份库：

`restic init --repo {{path/to/repository}}`

- 将一个目录备份到库中：

`restic --repo {{path/to/repository}} backup {{path/to/directory}}`

- 显示当前存储在库中的备份快照：

`restic --repo {{path/to/repository}} snapshots`

- 将特定的备份快照恢复到目标目录：

`restic --repo {{path/to/repository}} restore {{latest|snapshot_id}} --target {{path/to/target}}`

- 从特定备份中恢复特定路径到目标目录：

`restic --repo {{path/to/repository}} restore {{snapshot_id}} --target {{path/to/target}} --include {{path/to/restore}}`

- 清理备份库，仅保留每个唯一备份的最新快照：

`restic forget --keep-last 1 --prune`