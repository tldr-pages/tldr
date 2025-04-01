# debugfs

> 一个交互式的 ext2/ext3/ext4 文件系统调试器。
> 更多信息：<https://manned.org/debugfs>。

- 以只读模式打开文件系统：

`debugfs {{/dev/sdXN}}`

- 以读写模式打开文件系统：

`debugfs -w {{/dev/sdXN}}`

- 从指定文件读取命令并执行，然后退出：

`debugfs -f {{path/to/cmd_file}} {{/dev/sdXN}}`

- 在 debugfs 控制台中查看文件系统统计信息：

`stats`

- 关闭文件系统：

`close -a`

- 列出所有可用命令：

`lr`
