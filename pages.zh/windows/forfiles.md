# forfiles

> 选择一个或多个文件以执行指定的命令。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- 在当前的目录中寻找文件：

`forfiles`

- 在一个指定目录中寻找文件：

`forfiles /p {{目录的路径}}`

- 为每个文件执行指定的命令：

`forfiles /c "{{命令}}"`

- 使用通配符来寻找指定的文件：

`forfiles /m {{通配符}}`

- 递归寻找文件：

`forfiles /s`

- 搜索超过 5 天的文件：

`forfiles /d {{+5}}`
