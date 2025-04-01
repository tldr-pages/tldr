# sdcv

> StarDict，一个命令行词典客户端。
> 词典是与客户端分开提供的。
> 更多信息：<https://manned.org/sdcv>.

- 交互式启动 `sdcv`：

`sdcv`

- 列出已安装的词典：

`sdcv --list-dicts`

- 从特定词典中显示定义：

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- 使用模糊搜索查找定义：

`sdcv {{search_term}}`

- 使用精确搜索查找定义：

`sdcv --exact-search {{search_term}}`

- 查找定义并将输出格式化为 JSON：

`sdcv --json {{search_term}}`

- 在特定目录中搜索词典：

`sdcv --data-dir {{path/to/directory}} {{search_term}}`