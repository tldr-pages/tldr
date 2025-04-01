# replace

> 替换文件。
> 参见：`robocopy`、`move`、`copy` 和 `del`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/replace>。

- 使用源目录中的文件替换目标文件：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}}`

- 向目标目录添加文件，而不是替换现有文件：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}} /a`

- 在替换或添加目标文件之前进行提示，交互式复制多个文件：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}} /p`

- 替换只读文件：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}} /r`

- 等待插入磁盘后再替换文件（最初用于插入软盘）：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}} /w`

- 替换目标目录子目录中的所有文件：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}} /s`

- 仅替换目标目录中比源目录文件旧的文件：

`replace {{path\to\file_or_directory}} {{path\to\destination_directory}} /u`

- 显示帮助：

`replace /?`