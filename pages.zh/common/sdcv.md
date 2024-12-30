# sdcv

> StarDict，一个命令行字典客户端。
> 字典与客户端是分开提供的。
> 更多信息：<https://manned.org/sdcv>。

- 交互式启动 `sdcv`：

`sdcv`

- 列出已安装的字典：

`sdcv --list-dicts`

- 从特定字典中显示定义：

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- 进行模糊搜索查找定义：

`sdcv {{search_term}}`

- 进行精确搜索查找定义：

`sdcv --exact-search {{search_term}}`

- 查找定义并将输出格式化为 JSON：

`sdcv --json {{search_term}}`

- 在特定目录中搜索字典：

`sdcv --data-dir {{path/to/directory}} {{search_term}}`