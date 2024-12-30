# openconnect

> 一个用于Cisco AnyConnect VPN及其他VPN的客户端。
> 更多信息: <https://www.infradead.org/openconnect/manual.html>。

- 连接到服务器：

`openconnect {{vpn.example.org}}`

- 连接到服务器，并在后台运行：

`openconnect --background {{vpn.example.org}}`

- 终止在后台运行的连接：

`killall -SIGINT openconnect`

- 连接到服务器，从配置文件中读取选项：

`openconnect --config={{path/to/file}} {{vpn.example.org}}`

- 连接到服务器，并使用特定的SSL客户端证书进行身份验证：

`openconnect --certificate={{path/to/file}} {{vpn.example.org}}`