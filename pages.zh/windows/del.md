# del

> 删除一个或多个文件。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/del>.

- 删除一个或多个以空格分隔的文件：

`del {{文件 文件 ..}}`

- 在删除每个文件之前提示确认：

`del {{文件}} /p`

- 强制删除只读文件：

`del {{文件}} /f`

- 递归删除所有子目录中的文件：

`del {{文件}} /s`

- 在基于全局通配符删除文件时不提示确认：

`del {{文件}} /q`

- 显示帮助和所有的属性列表：

`del /?`

- 根据指定的属性删除文件：

`del {{文件}} /a {{属性}}`
