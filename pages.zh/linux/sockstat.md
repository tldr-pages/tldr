# sockstat

> 列出打开的互联网或 UNIX 域套接字。
> 另见：`netstat`。
> 更多信息：<https://manned.org/sockstat>。

- 显示 IPv4 和 IPv6 套接字的信息，包括监听和连接套接字：

`sockstat`

- 显示在特定端口上监听的 IPv[4]/IPv[6] 套接字的信息，使用特定的 p[R]otocol：

`sockstat -{{4|6}} -l -R {{tcp|udp|raw|unix}} -p {{port1,port2...}}`

- 还显示 [c]onnected 套接字和 [u]nix 套接字：

`sockstat -cu`

- 仅显示指定 `pid` 或进程的套接字：

`sockstat -P {{pid|process}}`

- 仅显示指定 `uid` 或用户的套接字：

`sockstat -U {{uid|user}}`

- 仅显示指定 `gid` 或组的套接字：

`sockstat -G {{gid|group}}`