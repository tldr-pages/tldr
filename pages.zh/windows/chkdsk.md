# chkdsk

> 检查文件系统和卷的元数据错误。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- 指定要检查的驱动器号（后跟冒号）、挂载点或卷名：

`chkdsk {{volume}}`

- 修复特定卷上的错误：

`chkdsk {{volume}} /f`

- 在检查之前卸载特定卷：

`chkdsk {{volume}} /x`

- 将日志文件大小更改到指定大小（仅适用于 NTFS）：

`chkdsk /l{{size}}`
