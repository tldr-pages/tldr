# del

> 删除一个或多个文件。
> 在 PowerShell 中，此命令为 `Remove-Item` 的別名。本页的描述是基于命令提示符 (`cmd`) 中的 `del`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- 查阅 PowerShell 的对应命令:

`tldr remove-item`

- 删除一个或多个文件 (可使用通配符)：

`del {{文件1 文件2 ...}}`

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
