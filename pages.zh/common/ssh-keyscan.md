# ssh-keyscan

> 获取远程主机的公共 SSH 密钥。
> 更多信息：<https://man.openbsd.org/ssh-keyscan>。

- 检索远程主机的所有公共 SSH 密钥：

`ssh-keyscan {{host}}`

- 检索在特定端口上监听的远程主机的所有公共 SSH 密钥：

`ssh-keyscan -p {{port}} {{host}}`

- 检索远程主机的某些类型的公共 SSH 密钥：

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{host}}`

- 手动使用给定主机的指纹更新 SSH known_hosts 文件：

`ssh-keyscan -H {{host}} >> ~/.ssh/known_hosts`