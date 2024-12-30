# gpgv

> 验证 OpenPGP 签名。
> 更多信息：<https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>。

- 验证一个签名文件：

`gpgv {{path/to/file}}`

- 使用分离签名验证一个签名文件：

`gpgv {{path/to/signature}} {{path/to/file}}`

- 将文件添加到密钥环列表中（单个导出的密钥也算作一个密钥环）：

`gpgv --keyring {{./alice.keyring}} {{path/to/signature}} {{path/to/file}}`