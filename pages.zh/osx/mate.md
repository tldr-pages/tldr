# mate

> 通用文本编辑器，适用于 macOS。
> 更多信息：<https://macromates.com/>。

- 启动 TextMate：

`mate`

- 打开特定文件：

`mate {{path/to/file1 path/to/file2 ...}}`

- 指定文件的文件类型：

`mate --type {{filetype}} {{path/to/file}}`

- 打开特定文件并在编辑完成前等待：

`mate --wait {{path/to/file}}`

- 以特定行和列的光标打开文件：

`mate --line {{line_number}}:{{column_number}} {{path/to/file}}`