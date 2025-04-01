# kate

> KDE 的高级文本编辑器。
> 更多信息：<https://kate-editor.org/>。

- 打开特定文件：

`kate {{path/to/file1 path/to/file2 ...}}`

- 打开特定的远程文件：

`kate {{https://example.com/path/to/file1 https://example.com/path/to/file2 ...}}`

- 即使已有实例打开，也要创建一个新的编辑器实例：

`kate --new`

- 打开文件并将光标定位到特定行：

`kate --line {{line_number}} {{path/to/file}}`

- 打开文件并将光标定位到特定行和列：

`kate --line {{line_number}} --column {{column_number}} {{path/to/file}}`

- 从 `stdin` 创建文件：

`cat {{path/to/file}} | kate --stdin`

- 显示帮助：

`kate --help`