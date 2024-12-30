# hash

> 查看缓存的可执行文件位置。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-hash>。

- 查看当前 shell 的缓存命令位置：

`hash`

- 清空哈希表：

`hash -r`

- 从哈希表中删除特定命令：

`hash -d {{command}}`

- 打印 `command` 的完整路径：

`hash -t {{command}}`