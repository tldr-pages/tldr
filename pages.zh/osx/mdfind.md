# mdfind

> 列出与查询匹配的文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/mdfind.1.html>。

- 按文件名查找文件：

`mdfind -name {{file}}`

- 按文件内容查找文件：

`mdfind "{{query}}"`

- 在指定目录中查找包含某个字符串的文件：

`mdfind -onlyin {{directory}} "{{query}}"`