# duplicacy

> 一款无锁的去重云备份工具。
> 更多信息：<https://github.com/gilbertchen/duplicacy/wiki>。

- 使用当前目录作为仓库，初始化一个 SFTP 存储并使用密码加密存储：

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

- 删除特定修订版的快照：

`duplicacy prune -r {{revision}}`

- 修剪修订版，对于所有超过 `m` 天的修订版，保留每 `n` 天的一个修订版：

`duplicacy prune -keep {{n:m}}`