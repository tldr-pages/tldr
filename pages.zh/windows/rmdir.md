# rmdir

> 删除一个目录和其中的内容。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 删除一个空目录：

`rmdir {{目录的路径}}`

- 递归删除一个目录及其中的内容：

`rmdir {{目录的路径}} /s`

- 在没有提示的情况下递归删除目录及其内容：

`rmdir {{path/to/directory}} /s /q`
