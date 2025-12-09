# rmdir

> 删除目录及其内容。
> 在 PowerShell 中，此命令是 `Remove-Item` 的别名。此文档基于 `cmd` 版本的 `rmdir`。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 查看等效的 PowerShell 命令的文档：

`tldr remove-item`

- 删除一个空目录：

`rmdir {{路径\到\目录}}`

- 递归删除目录及其内容：

`rmdir {{路径\到\目录}} /s`

- 递归删除目录及其内容，无需提示：

`rmdir {{路径\到\目录}} /s /q`
