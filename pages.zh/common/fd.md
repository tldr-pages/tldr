# fd

> `find` 的替代方案。
> 旨在比 `find` 更快且更易于使用。
> 更多信息：<https://github.com/sharkdp/fd>。

- 在当前目录中递归查找匹配特定模式的文件：

`fd "{{string|regex}}"`

- 查找以特定字符串开头的文件：

`fd "{{^string}}"`

- 查找具有特定扩展名的文件：

`fd --extension {{txt}}`

- 在特定目录中查找文件：

`fd "{{string|regex}}" {{path/to/directory}}`

- 在搜索中包含被忽略和隐藏的文件：

`fd --hidden --no-ignore "{{string|regex}}"`

- 对每个返回的搜索结果执行命令：

`fd "{{string|regex}}" --exec {{command}}`