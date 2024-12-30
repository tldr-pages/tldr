# paperkey

> 一个 OpenPGP 密钥归档工具。
> 更多信息：<https://www.jabberwocky.com/software/paperkey/>。

- 获取特定的秘密密钥并生成包含秘密数据的文本文件：

`paperkey --secret-key {{path/to/secret_key.gpg}} --output {{path/to/secret_data.txt}}`

- 获取 `secret_data.txt` 中的秘密密钥数据，并与公钥结合以重建秘密密钥：

`paperkey --pubring {{path/to/public_key.gpg}} --secrets {{path/to/secret_data.txt}} --output {{secret_key.gpg}}`

- 导出特定的秘密密钥并生成包含秘密数据的文本文件：

`gpg --export-secret-key {{key}} | paperkey --output {{path/to/secret_data.txt}}`