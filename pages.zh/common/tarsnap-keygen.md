# tarsnap-keygen

> 为 Tarsnap（一个在线备份服务）生成密钥文件。
> 更多信息：<https://www.tarsnap.com/man-tarsnap-keygen.1.html>。

- 在 Tarsnap 服务器上注册一台机器：

`sudo tarsnap-keygen --keyfile {{path/to/file.key}} --user {{user_email}} --machine {{machine_name}}`

- 加密密钥文件（将要求输入密码短语两次）：

`sudo tarsnap-keygen --keyfile {{path/to/file.key}} --user {{user_email}} --machine {{machine_name}} --passphrased`