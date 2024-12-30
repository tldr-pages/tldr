# clip

> 将输入内容复制到 Windows 剪贴板。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/clip>。

- 将命令行输出通过管道发送到 Windows 剪贴板：

`{{dir}} | clip`

- 将文件的内容复制到 Windows 剪贴板：

`clip < {{path\to\file.ext}}`

- 将带有换行符的文本复制到 Windows 剪贴板：

`echo {{some text}} | clip`

- 将不带换行符的文本复制到 Windows 剪贴板：

`echo | set /p="some text" | clip`