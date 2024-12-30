# gpg2

> GNU 隐私保护工具 2。
> 有关 GNU 隐私保护工具 1 的信息，请参见 `gpg`。
> 更多信息：<https://docs.releng.linuxfoundation.org/en/latest/gpg.html>。

- 列出导入的密钥：

`gpg2 --list-keys`

- 为指定的收件人加密指定的文件，并将输出写入一个新文件，文件名后附加 `.gpg`：

`gpg2 --encrypt --recipient {{alice@example.com}} {{path/to/doc.txt}}`

- 仅使用密码短语加密指定的文件，并将输出写入一个新文件，文件名后附加 `.gpg`：

`gpg2 --symmetric {{path/to/doc.txt}}`

- 解密指定的文件，并将结果写入 `stdout`：

`gpg2 --decrypt {{path/to/doc.txt.gpg}}`

- 导入公钥：

`gpg2 --import {{path/to/public_key.gpg}}`

- 将指定电子邮件地址的公钥导出到 `stdout`：

`gpg2 --export --armor {{alice@example.com}}`

- 将指定电子邮件地址的私钥导出到 `stdout`：

`gpg2 --export-secret-keys --armor {{alice@example.com}}`