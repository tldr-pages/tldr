# rmdir

> 删除目录及其内容。
> 在 PowerShell 中，此命令是 `Remove-Item` 的别名。本文档基于命令提示符（`cmd`）版本的 `rmdir`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>。

- 查看等效 PowerShell 命令的文档：

`tldr remove-item`

- 删除一个空目录：

`rmdir {{path\to\directory}}`

- 递归删除目录及其内容：

`rmdir {{path\to\directory}} /s`

- 递归删除目录及其内容而不提示：

`rmdir {{path\to\directory}} /s /q`