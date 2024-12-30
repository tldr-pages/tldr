# cipher

> 显示或更改 NTFS 卷上目录和文件的加密。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>。

- 显示特定加密文件或目录的信息：

`cipher /c:{{path\to\file_or_directory}}`

- [e]ncrypt（加密）一个文件或目录（后来添加到该目录的文件也会被加密，因为该目录已被标记为加密）：

`cipher /e:{{path\to\file_or_directory}}`

- [d]ecrypt（解密）一个文件或目录：

`cipher /d:{{path\to\file_or_directory}}`

- 安全地删除一个文件或目录：

`cipher /w:{{path\to\file_or_directory}}`