# cryptcat

> Cryptcat 是带有加密功能的 netcat。
> 更多信息：<https://manned.org/cryptcat>。

- [l]监听指定的[p]端口并打印接收到的任何数据：

`cryptcat -k {{password}} -l -p {{port}}`

- 连接到指定端口：

`cryptcat -k {{password}} {{ip_address}} {{port}}`

- 指定超时时间([w])：

`cryptcat -k {{password}} -w {{timeout_in_seconds}} {{ip_address}} {{port}}`

- 扫描([z])指定主机的开放端口：

`cryptcat -v -z {{ip_address}} {{port}}`

- 作为代理，将本地 TCP 端口的数据转发到给定的远程主机：

`cryptcat -k {{password}} -l -p {{local_port}} | cryptcat -k {{password}} {{hostname}} {{remote_port}}`
