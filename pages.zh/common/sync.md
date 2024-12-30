# 同步

> 将所有待处理的写入操作刷新到相应的磁盘。
> 更多信息：<https://www.gnu.org/software/coreutils/sync>。

- 刷新所有磁盘上的所有待处理写入操作：

`sync`

- 将单个文件的所有待处理写入操作刷新到磁盘：

`sync {{path/to/file}}`