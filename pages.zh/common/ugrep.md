# ugrep

> 超快速搜索工具，带有查询 TUI。
> 更多信息：<https://github.com/Genivia/ugrep>。

- 启动查询 TUI，以递归方式搜索当前目录中的文件（CTRL-Z 获取帮助）：

`ugrep --query`

- 在当前目录中递归搜索包含正则表达式搜索模式的文件：

`ugrep "{{search_pattern}}"`

- 在特定文件或特定目录中的所有文件中搜索，并显示匹配行的行号：

`ugrep --line-number "{{search_pattern}}" {{path/to/file_or_directory}}`

- 在当前目录中的所有文件中递归搜索，并打印每个匹配文件的名称：

`ugrep --files-with-matches "{{search_pattern}}"`

- 模糊搜索文件，允许模式中最多有 3 个额外的、缺失的或不匹配的字符：

`ugrep --fuzzy={{3}} "{{search_pattern}}"`

- 还可以递归搜索压缩文件、Zip 和 tar 归档：

`ugrep --decompress "{{search_pattern}}"`

- 仅搜索文件名匹配特定通配符模式的文件：

`ugrep --glob="{{glob_pattern}}" "{{search_pattern}}"`

- 仅搜索 C++ 源文件（使用 `--file-type=list` 列出所有文件类型）：

`ugrep --file-type=cpp "{{search_pattern}}"`