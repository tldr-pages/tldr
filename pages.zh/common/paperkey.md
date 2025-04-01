# paperkey

> 一个 OpenPGP 密钥存档工具。
> 更多信息：<https://www.jabberwocky.com/software/paperkey/>.

- 使用特定的私钥生成包含私钥数据的文本文件：

`paperkey --secret-key {{path/to/secret_key.gpg}} --output {{path/to/secret_data.txt}}`

- 使用 `secret_data.txt` 中的私钥数据，结合公钥重新构建私钥：

`paperkey --pubring {{path/to/public_key.gpg}} --secrets {{path/to/secret_data.txt}} --output {{secret_key.gpg}}`

- 导出特定的私钥并生成包含私钥数据的文本文件：

`gpg --export-secret-key {{key}} | paperkey --output {{path/to/secret_data.txt}}`