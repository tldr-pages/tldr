# dbclient

> 轻量级的 Dropbear 安全Shell客户端。
> 更多信息：<https://manned.org/dbclient>。

- 连接到远程主机：

`dbclient {{user}}@{{host}}`

- 连接到远程主机的 [p]ort 2222 端口：

`dbclient {{user}}@{{host}} -p 2222`

- 使用特定的 [i]dentity 密钥（dropbear格式）连接到远程主机：

`dbclient -i {{path/to/key_file}} {{user}}@{{host}}`

- 在远程主机上运行命令，分配 [t]ty 以允许与远程命令交互：

`dbclient {{user}}@{{host}} -t {{command}} {{argument1 argument2 ...}}`

- 连接并转发 [A]gent 连接到远程主机：

`dbclient -A {{user}}@{{host}}`