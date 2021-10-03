# find

> 在一个或多个文件里查找指定字符串。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/find>.

- 查找包含指定字符串的行：

`find {{字符串}} {{文件或目录的路径}}`

- 查找不包含指定字符串的行：

`find {{字符串}} {{文件或目录的路径}} /v`

- 显示包含指定字符串的行的总数：

`find {{字符串}} {{文件或目录的路径}} /c`

- 显示匹配的行的行数：

`find {{字符串}} {{文件或目录的路径}} /n`
