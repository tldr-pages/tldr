# mdfind

> 列出与给定查询匹配的文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- 按文件名查找文件：

`mdfind -name {{文件}}`

- 按内容查找文件：

`mdfind "{{查找的字符串}}"`

- 在给定目录中查找包含字符串的文件：

`mdfind -onlyin {{目录}} "{{字符串}}"`
