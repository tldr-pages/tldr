# forfiles

> 选择要对其执行指定命令的文件。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>。

- 在当前目录中搜索文件：

`forfiles`

- 在特定目录中搜索文件：

`forfiles /p {{path\to\directory}}`

- 对每个文件运行指定的命令：

`forfiles /c "{{command}}"`

- 使用特定的全局掩码搜索文件：

`forfiles /m {{glob_pattern}}`

- 递归搜索文件：

`forfiles /s`

- 搜索超过 5 天的文件：

`forfiles /d +{{5}}`