# sockstat

> 列出打开的 Internet 或 UNIX 域套接字。
> 另见：`netstat`。
> 更多信息：<https://manned.org/sockstat>。

- 显示 IPv4 和 IPv6 套接字的监听和连接信息：

`sockstat`

- 显示 IPv[4]/IPv[6] 套接字在特定端口上使用特定[Y]协议的[l]监听信息：

`sockstat -{{4|6}} -l -R {{tcp|udp|raw|unix}} -p {{port1,port2...}}`

- 显示连接的套接字和 UNIX 套接字：

`sockstat -cu`

- 仅显示指定 `pid` 或进程的套接字：

`sockstat -P {{pid|process}}`

- 仅显示指定 `uid` 或用户的套接字：

`sockstat -U {{uid|user}}`

- 仅显示指定 `gid` 或组的套接字：

`sockstat -G {{gid|group}}`