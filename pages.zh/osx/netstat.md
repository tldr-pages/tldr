# netstat

> 显示与网络相关的信息，如开放连接、开放的套接字端口等。
> 另见：`lsof` 用于列出网络连接，包括监听端口。
> 更多信息：<https://keith.github.io/xcode-man-pages/netstat.1.html>。

- 显示监听特定协议的进程 ID 和程序名称：

`netstat -p {{protocol}}`

- 打印路由表，并且不将 IP 地址解析为主机名：

`netstat -nr`

- 打印 IPv4 地址的路由表：

`netstat -nr -f inet`