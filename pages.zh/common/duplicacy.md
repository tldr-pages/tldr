# duplicacy

> 一个无锁去重的云备份工具。
> 更多信息：<https://github.com/gilbertchen/duplicacy/wiki>.

- 使用当前目录作为仓库，初始化一个 SFTP 存储，并使用密码加密存储：

`duplicacy init -e {{snapshot_id}} {{sftp://user@192.168.2.100/path/to/storage/}}`

- 将仓库的快照保存到默认存储：

`duplicacy backup`

- 列出当前仓库的快照：

`duplicacy list`

- 将仓库恢复到之前保存的快照：

`duplicacy restore -r {{revision}}`

- 检查快照的完整性：

`duplicacy check`

- 为现有仓库添加另一个存储：

`duplicacy add {{storage_name}} {{snapshot_id}} {{storage_url}}`

- 清理特定版本的快照：

`duplicacy prune -r {{revision}}`

- 清理版本，保留 `m` 天之前每个 `n` 天的一个版本：

`duplicacy prune -keep {{n:m}}`