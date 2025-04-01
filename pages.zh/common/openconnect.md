# openconnect

> 一款用于 Cisco AnyConnect 及其他类似 VPN 的客户端。
> 更多信息：<https://www.infradead.org/openconnect/manual.html>。

- 连接到服务器：

`openconnect {{vpn.example.org}}`

- 连接到服务器，进程在后台运行：

`openconnect --background {{vpn.example.org}}`

- 终止后台运行的连接：

`killall -SIGINT openconnect`

- 连接到服务器，从配置文件中读取选项：

`openconnect --config={{path/to/file}} {{vpn.example.org}}`

- 连接到服务器并使用特定的 SSL 客户端证书进行身份验证：

`openconnect --certificate={{path/to/file}} {{vpn.example.org}}`