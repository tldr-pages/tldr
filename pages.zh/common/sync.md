# sync

> 将所有待处理的写入操作刷新到相应的磁盘。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sync-invocation.html>。

- 刷新所有磁盘上的待处理写入操作：

`sync`

- 将单个文件的待处理写入操作刷新到磁盘：

`sync {{路径/到/文件}}`

- 刷新写入并丢弃文件系统缓存（仅 Linux）：

`sync; echo 3 | sudo tee /proc/sys/vm/drop_caches`

- 刷新磁盘写入并尝试清除非活动内存和文件系统缓存（仅 macOS）：

`sync; sudo purge`
