# hash

> 查看缓存的可执行文件位置。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-hash>。

- 查看当前 shell 中缓存的命令位置：

`hash`

- 清除哈希表：

`hash -r`

- 从哈希表中删除特定命令：

`hash -d {{command}}`

- 打印 `command` 的完整路径：

`hash -t {{command}}`

- 显示帮助信息：

`hash --help`