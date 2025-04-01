# netstat

> 显示与网络相关的信息，如打开的连接、打开的套接字端口等。
> 参见：`lsof` 用于列出网络连接，包括监听端口。
> 更多信息：<https://keith.github.io/xcode-man-pages/netstat.1.html>.

- 显示监听特定协议的 PID 和程序名称：

`netstat -p {{protocol}}`

- 打印路由表，不将 IP 地址解析为主机名：

`netstat -nr`

- 打印 IPv4 地址的路由表：

`netstat -nr -f inet`
