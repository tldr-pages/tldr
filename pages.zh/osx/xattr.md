# xattr

> 用于扩展文件系统属性的实用程序。
> 更多信息：<https://keith.github.io/xcode-man-pages/xattr.1.html>.

- 列出 键：值 列表，显示指定文件的值扩展属性：

`xattr -l {{文件名}}`

- 为给定文件写入属性：

`xattr -w {{属性键名}} {{属性值}} {{文件名}}`

- 从给定文件中删除属性：

`xattr -d {{com.apple.quarantine}} {{文件名}}`

- 从给定文件中删除所有扩展属性：

`xattr -c {{文件名}}`

- 递归删除给定目录中文件的属性：

`xattr -rd {{属性键名}} {{目录}}`
