# sockstat

> 列出打开的互联网或UNIX域套接字。
> 注意：该程序是为NetBSD 3.0重新编写的，源自FreeBSD的`sockstat`。
> 另见：`netstat`。
> 更多信息：<https://man.netbsd.org/sockstat.1>。

- 显示IPv4、IPv6和Unix套接字的监听和连接状态的信息：

`sockstat`

- 显示在特定端口上监听的IPv[4]/IPv[6]套接字的信息，使用特定协议：

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- 也显示连接的套接字，显示UNIX套接字：

`sockstat -cu`

- 仅显示数字输出，不解析地址和端口的符号名称：

`sockstat -n`

- 仅列出指定地址族的套接字：

`sockstat -f {{inet|inet6|local|unix}}`