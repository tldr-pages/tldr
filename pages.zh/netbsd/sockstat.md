# sockstat

> 列出打开的 Internet 或 UNIX 域套接字。
> 注意：此程序是在 NetBSD 3.0 中从 FreeBSD 的 `sockstat` 重写的。
> 参见：`netstat`。
> 更多信息：<https://man.netbsd.org/sockstat.1>。

- 显示 IPv4、IPv6 和 Unix 套接字的信息，包括监听和已连接的套接字：

`sockstat`

- 显示 IPv[4]/IPv[6] 套接字在特定 [p]ort 上通过特定 [P]rotocol [l]istening 的信息：

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- 同时显示 [c]onnected 套接字，显示 [u]nix 套接字：

`sockstat -cu`

- 只显示 [n]umeric 输出，不解析地址和端口的符号名称：

`sockstat -n`

- 仅列出指定地址 [f]amily 的套接字：

`sockstat -f {{inet|inet6|local|unix}}`
