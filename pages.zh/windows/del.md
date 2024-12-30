# del

> 删除一个或多个文件。
> 在 PowerShell 中，此命令是 `Remove-Item` 的别名。本文件基于命令提示符（`cmd`）版本的 `del`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/del>。

- 查看等效 PowerShell 命令的文档：

`tldr remove-item`

- 删除一个或多个文件或模式：

`del {{file_pattern1 file_pattern2 ...}}`

- 在删除每个文件之前提示确认：

`del {{file_pattern}} /p`

- 强制删除只读文件：

`del {{file_pattern}} /f`

- 递归删除所有子目录中的文件：

`del {{file_pattern}} /s`

- 基于全局通配符删除文件时不提示：

`del {{file_pattern}} /q`

- 显示帮助并列出可用属性：

`del /?`

- 根据指定属性删除文件：

`del {{file_pattern}} /a {{attribute}}`