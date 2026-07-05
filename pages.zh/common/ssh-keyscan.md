# ssh-keyscan

> 获取远程主机的 SSH 公钥。
> 更多信息：<https://man.openbsd.org/ssh-keyscan>。

- 获取远程主机的所有 SSH 公钥：

`ssh-keyscan {{主机名}}`

- 获取监听特定端口的远程主机的所有 SSH 公钥：

`ssh-keyscan -p {{端口}} {{主机名}}`

- 获取远程主机上特定类型的 SSH 公钥：

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{主机名}}`

- 使用给定主机的指纹手动更新 SSH `known_hosts` 文件：

`ssh-keyscan -H {{主机名}} >> ~/.ssh/known_hosts`
