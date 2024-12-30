# lbu

> 管理无磁盘的 Alpine Linux 系统上的 `apk` 覆盖文件。
> 注意：像 `include` 这样的子命令会写入 `/etc`，该目录存储在 RAM 中。您需要运行 `lbu commit` 来保存更改。
> 更多信息：<https://wiki.alpinelinux.org/wiki/Alpine_local_backup>。

- 提交更改到持久存储（默认情况下只包含 `/etc` 中的文件）：

`lbu {{ci|commit}}`

- 列出使用 `commit` 将要保存的文件：

`lbu {{st|status}}`

- 显示将要使用 `commit` 保存的跟踪文件的更改：

`lbu diff`

- 在 `apk` 覆盖中包含特定文件或目录：

`lbu {{add|inc|include}} {{path/to/file_or_directory}}`

- 从 `apk` 覆盖中排除 `/etc` 中的特定文件或目录：

`lbu {{ex|exclude|delete}} {{path/to/file_or_directory}}`

- 显示手动包含/排除的文件列表：

`lbu {{inc|include|ex|exclude}} -l`

- 列出备份（之前创建的覆盖）：

`lbu {{lb|list-backup}}`

- 恢复到备份覆盖：

`lbu revert {{overlay_filename.tar.gz}}`