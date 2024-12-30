# ag

> 银色搜索器。像 `ack`，但旨在更快。
> 更多信息：<https://github.com/ggreer/the_silver_searcher>。

- 查找包含 "foo" 的文件，并打印上下文中的匹配行：

`ag {{foo}}`

- 在特定目录中查找包含 "foo" 的文件：

`ag {{foo}} {{path/to/directory}}`

- 查找包含 "foo" 的文件，但仅列出文件名：

`ag -l {{foo}}`

- 查找不区分大小写的 "FOO"，并仅打印匹配项，而不是整行：

`ag -i -o {{FOO}}`

- 在名称匹配 "bar" 的文件中查找 "foo"：

`ag {{foo}} -G {{bar}}`

- 查找内容匹配正则表达式的文件：

`ag '{{^ba(r|z)$}}'`

- 查找名称匹配 "foo" 的文件：

`ag -g {{foo}}`