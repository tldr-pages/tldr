# mate-search-tool

> 在MATE桌面环境中搜索文件。
> 更多信息：<https://manned.org/mate-search-tool>。

- 在特定目录中搜索文件名包含特定字符串的文件：

`mate-search-tool --named={{string}} --path={{path/to/directory}}`

- 无需等待用户确认搜索文件：

`mate-search-tool --start --named={{string}} --path={{path/to/directory}}`

- 搜索文件名匹配特定正则表达式的文件：

`mate-search-tool --start --regex={{string}} --path={{path/to/directory}}`

- 在搜索结果中设置排序顺序：

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --sortby={{name|folder|size|type|date}}`

- 设置降序排序：

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --descending`

- 搜索由特定用户/组拥有的文件：

`mate-search-tool --start --{{user|group}}={{value}} --path={{path/to/directory}}`