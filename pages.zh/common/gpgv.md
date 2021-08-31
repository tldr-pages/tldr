# gpgv

> 验证 OpenPGP 签名。
> 更多信息：<https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- 验证签名文件：

`gpgv {{path/to/file}}`

- 使用分离式签名验证已签名的文件：

`gpgv {{path/to/signature}} {{path/to/file}}`

- 在 keyrings 列表中添加一个文件（一个导出的钥匙也算作一个 keyring）：

`gpgv --keyring {{path/to/keyring_file}} {{path/to/signature}} {{path/to/file}}`
