# dir

> 使用每行一个文件来列出目录内容，特殊字符以反斜杠转义序列表示。
> 作用类似于 `ls -C --escape`。
> 更多信息：<https://manned.org/dir>.

- 列出包含隐藏文件的所有文件：

`dir {{[-a|--all]}}`

- 列出文件，包括作者信息（需要 `-l` 参数）：

`dir -l --author`

- 列出文件，排除符合指定模式的文件：

`dir --hide {{pattern}}`

- 递归列出子目录：

`dir {{[-R|--recursive]}}`

- 显示帮助信息：

`dir --help`