# lbu

> 管理无盘 Alpine Linux 系统上的 `apk` 覆盖文件。
> 注意：像 `include` 这样的子命令会写入 `/etc` 目录，该目录存储在 RAM 中。你需要运行 `lbu commit` 来保存更改。
> 更多信息：<https://wiki.alpinelinux.org/wiki/Alpine_local_backup>.

- 将更改提交到持久存储（默认仅保存 `/etc` 目录中的文件）：

`lbu {{[ci|commit]}}`

- 列出使用 `commit` 将要保存的文件：

`lbu {{[st|status]}}`

- 显示使用 `commit` 将要保存的跟踪文件的更改：

`lbu diff`

- 将特定文件或目录包含在 `apk` 覆盖中：

`lbu {{[inc|include]}} {{path/to/file_or_directory}}`

- 从 `apk` 覆盖中排除 `/etc` 目录中的特定文件或目录：

`lbu {{[ex|exclude]}} {{path/to/file_or_directory}}`

- 显示手动包含/排除的文件列表：

`lbu {{include|exclude}} -l`

- 列出备份（之前创建的覆盖文件）：

`lbu {{[lb|list-backup]}}`

- 回滚到备份覆盖文件：

`lbu revert {{overlay_filename.tar.gz}}`