# e2undo

> 重放 ext2/ext3/ext4 文件系统的撤销日志。
> 这可以用于撤销 e2fsprogs 程序的失败操作。
> 更多信息：<https://manned.org/e2undo>。

- 显示特定撤销文件的信息：

`e2undo -h {{path/to/undo_file}} {{/dev/sdXN}}`

- 执行干运行并显示可重放的候选块：

`e2undo -nv {{path/to/undo_file}} {{/dev/sdXN}}`

- 执行撤销操作：

`e2undo {{path/to/undo_file}} {{/dev/sdXN}}`

- 执行撤销操作并显示详细信息：

`e2undo -v {{path/to/undo_file}} {{/dev/sdXN}}`

- 在覆盖文件系统块之前，将块的旧内容写入撤销文件：

`e2undo -z {{path/to/file.e2undo}} {{path/to/undo_file}} {{/dev/sdXN}}`