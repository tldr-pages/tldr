# age

> 一个简单、现代和安全的文件加密工具。
> 另见：`age-keygen` 用于生成密钥对。
> 更多信息：<https://github.com/FiloSottile/age>。

- 生成一个可以用密码解密的加密文件：

`age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- 使用一个或多个作为字面值输入的公钥加密文件（重复 `--recipient` 标志以指定多个公钥）：

`age --recipient {{public_key}} --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- 使用在文件中指定的公钥（每行一个）加密文件给一个或多个接收者：

`age --recipients-file {{path/to/recipients_file}} --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- 使用密码解密文件：

`age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`

- 使用私钥文件解密文件：

`age --decrypt --identity {{path/to/private_key_file}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`