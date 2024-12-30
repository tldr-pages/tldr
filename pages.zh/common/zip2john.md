# zip2john

> 从Zip档案中提取密码哈希，以供John the Ripper密码破解工具使用。
> 这是一个实用工具，通常作为John the Ripper安装的一部分进行安装。
> 更多信息：<https://www.openwall.com/john/>。

- 从档案中提取密码哈希，并列出档案中的所有文件：

`zip2john {{path/to/file.zip}}`

- 仅使用特定的压缩文件提取密码哈希：

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}}`

- 从压缩文件提取密码哈希到特定文件（供John the Ripper使用）：

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}} > {{file.hash}}`