# 获取文件哈希

> 计算文件的哈希值。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>。

- 使用 SHA256 算法计算指定文件的哈希值：

`Get-FileHash {{路径\到\文件}}`

- 使用指定算法计算指定文件的哈希值：

`Get-FileHash {{路径\到\文件}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`