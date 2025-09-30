# ugrep

> 超快速搜索工具，带有查询 TUI。
> 更多信息：<https://github.com/Genivia/ugrep>.

- 启动查询 TUI，在当前目录中递归搜索文件（按 `<Ctrl z>` 获取帮助）：

`ugrep --query`

- 在当前目录中递归搜索包含正则表达式搜索模式的文件：

`ugrep "{{search_pattern}}"`

- 在特定文件或特定目录中的所有文件中搜索，并显示匹配的行号：

`ugrep --line-number "{{search_pattern}}" {{路径/到/文件或目录}}`

- 递归搜索当前目录中的所有文件，并打印每个匹配文件的名称：

`ugrep --files-with-matches "{{search_pattern}}"`

- 模糊搜索文件，允许模式中多达 3 个额外、缺失或不匹配的字符：

`ugrep --fuzzy={{3}} "{{search_pattern}}"`

- 也递归搜索压缩文件、Zip 和 tar 存档：

`ugrep --decompress "{{search_pattern}}"`

- 仅搜索文件名匹配特定 glob 模式的文件：

`ugrep --glob="{{glob_pattern}}" "{{search_pattern}}"`

- 仅搜索 C++ 源文件（使用 `--file-type=list` 列出所有文件类型）：

`ugrep --file-type=cpp "{{search_pattern}}"`
