# es

> Everything 的命令行接口，一个快速的 Windows 文件和文件夹搜索工具。
> 需要安装并后台运行 Everything。
> 更多信息：<https://www.voidtools.com/support/everything/command_line_interface/>.

- 按名称搜索文件或文件夹：

`es {{search_term}}`

- 使用正则表达式搜索：

`es -r {{regex_pattern}}`

- 匹配完整单词：

`es -w {{search_term}}`

- 限制显示的结果数量：

`es -n {{10}} {{search_term}}`

- 在特定文件夹中搜索：

`es -path {{folder_path}} {{search_term}}`

- 仅列出文件夹：

`es /ad`

- 仅列出文件：

`es /a-d`

- 排序结果（例如，按名称）：

`es -sort {{name-ascending}}`