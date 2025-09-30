# zip2john

> 从 Zip 压缩文件中提取密码哈希，供 John the Ripper 密码破解程序使用。
> 这是一个通常作为 John the Ripper 安装的一部分安装的实用工具。
> 更多信息：<https://www.openwall.com/john/>.

- 从一个压缩文件中提取密码哈希，列出压缩文件中的所有文件：

`zip2john {{路径/到/文件.zip}}`

- 仅使用特定压缩文件提取密码哈希：

`zip2john -o {{路径/到/压缩_文件}} {{路径/到/文件.zip}}`

- 从压缩文件中提取密码哈希到一个特定文件（供 John the Ripper 使用）：

`zip2john -o {{路径/到/压缩_文件}} {{路径/到/文件.zip}} > {{文件.hash}}`
