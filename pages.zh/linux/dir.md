# dir

> 使用每个文件一行的方式列出目录内容，特殊字符由反斜杠转义序列表示。
> 工作方式类似于 `ls -C --escape`。
> 更多信息：<https://manned.org/dir>。

- 列出所有文件，包括隐藏文件：

`dir --all`

- 列出文件及其作者（需要 `-l`）：

`dir -l --author`

- 列出不匹配指定模式的文件：

`dir --hide={{pattern}}`

- 递归列出子目录：

`dir --recursive`

- 显示帮助信息：

`dir --help`