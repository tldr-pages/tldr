# Get-FileHash

> 计算一个文件的 HASH 值。
> 更多信息：<https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- 使用 SHA256 算法计算给定文件的哈希值：

`Get-FileHash {{文件路径}}`

- 使用指定的哈希算法计算给定文件的哈希值：

`Get-FileHash {{文件路径}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
