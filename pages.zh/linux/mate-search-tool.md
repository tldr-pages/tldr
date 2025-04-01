# mate-search-tool

> 在 MATE 桌面环境中搜索文件。
> 更多信息：<https://manned.org/mate-search-tool>.

- 在指定目录中搜索文件名包含特定字符串的文件：

`mate-search-tool --named={{string}} --path={{path/to/directory}}`

- 搜索文件时不等待用户确认：

`mate-search-tool --start --named={{string}} --path={{path/to/directory}}`

- 搜索文件名匹配特定正则表达式的文件：

`mate-search-tool --start --regex={{string}} --path={{path/to/directory}}`

- 设置搜索结果的排序方式：

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --sortby={{name|folder|size|type|date}}`

- 设置降序排序：

`mate-search-tool --start --named={{string}} --path={{path/to/directory}} --descending`

- 搜索特定用户或组拥有的文件：

`mate-search-tool --start --{{user|group}}={{value}} --path={{path/to/directory}}`
