# ack

> 一种类似于 `grep` 的搜索工具，专为开发人员优化。
> 另见：`rg`，速度更快。
> 更多信息：<https://beyondgrep.com/documentation>。

- 在当前目录递归搜索包含字符串或正则表达式的文件：

`ack "{{search_pattern}}"`

- 搜索不区分大小写的模式：

`ack --ignore-case "{{search_pattern}}"`

- 搜索匹配某个模式的行，仅打印匹配的文本而不打印行的其余部分：

`ack -o "{{search_pattern}}"`

- 限制搜索特定类型的文件：

`ack --type {{ruby}} "{{search_pattern}}"`

- 不在特定类型的文件中搜索：

`ack --type no{{ruby}} "{{search_pattern}}"`

- 统计找到的匹配总数：

`ack --count --no-filename "{{search_pattern}}"`

- 仅打印文件名和每个文件的匹配数量：

`ack --count --files-with-matches "{{search_pattern}}"`

- 列出所有可以与 `--type` 一起使用的值：

`ack --help-types`