# mosh

> Mobile Shell (`mosh`) 是 SSH 的一个强大且响应迅速的替代品。
> `mosh` 在不同网络间漫游时仍能保持与远程服务器的连接。
> 更多信息：<https://mosh.org>。

- 连接到远程服务器：

`mosh {{username}}@{{remote_host}}`

- 使用特定身份（私钥）连接到远程服务器：

`mosh --ssh="ssh -i {{path/to/key_file}}" {{username}}@{{remote_host}}`

- 使用特定端口连接到远程服务器：

`mosh --ssh="ssh -p {{2222}}" {{username}}@{{remote_host}}`

- 在远程服务器上运行命令：

`mosh {{remote_host}} -- {{command -with -flags}}`

- 选择 Mosh UDP 端口（当 `remote_host` 位于 NAT 后面时有用）：

`mosh -p {{124}} {{username}}@{{remote_host}}`

- 当 `mosh-server` 二进制文件不在标准路径中时的用法：

`mosh --server={{path/to/bin/}}mosh-server {{remote_host}}`