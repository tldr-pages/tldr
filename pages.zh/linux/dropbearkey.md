# dropbearkey

> 生成 Dropbear 格式的 SSH 密钥。
> 更多信息：<https://manned.org/dropbearkey>.

- 生成类型为 ed25519 的 SSH 密钥，并将其写入密钥文件：

`dropbearkey -t {{ed25519}} -f {{path/to/key_file}}`

- 生成类型为 ecdsa 的 SSH 密钥，并将其写入密钥文件：

`dropbearkey -t {{ecdsa}} -f {{path/to/key_file}}`

- 生成类型为 RSA、密钥大小为 4096 位的 SSH 密钥，并将其写入密钥文件：

`dropbearkey -t {{rsa}} -s {{4096}} -f {{path/to/key_file}}`

- 打印密钥文件中的私钥指纹和公钥：

`dropbearkey -y -f {{path/to/key_file}}`
