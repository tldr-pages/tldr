# xattr

> 用于处理扩展文件系统属性的工具。
> 更多信息：<https://keith.github.io/xcode-man-pages/xattr.1.html>。

- 列出给定文件的键值扩展属性：

`xattr -l {{file}}`

- 为给定文件写入属性：

`xattr -w {{attribute_key}} {{attribute_value}} {{file}}`

- 从给定文件中删除属性：

`xattr -d {{com.apple.quarantine}} {{file}}`

- 从给定文件中删除所有扩展属性：

`xattr -c {{file}}`

- 递归删除给定目录中的属性：

`xattr -rd {{attribute_key}} {{directory}}`