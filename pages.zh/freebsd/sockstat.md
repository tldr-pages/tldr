# sockstat

> 列出打开的 Internet 或 UNIX 域套接字。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?sockstat>。

- 显示哪些用户/进程正在监听哪些端口：

`sockstat -l`

- 显示使用特定协议监听特定端口的 IPv[4]/IPv[6] 套接字信息：

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- 显示已连接的套接字，不解析数字 UID 为用户名，并使用更宽的字段大小：

`sockstat -cnw`

- 仅显示属于特定 [j]ail ID 或名称的套接字，并以详细模式显示：

`sockstat -jv`

- 显示协议状态和远程 UDP 封装端口号（如适用）（目前仅在 SCTP 和 TCP 中实现）：

`sockstat -sU`

- 显示拥塞控制模块和协议栈（如适用）（目前仅在 TCP 中实现）：

`sockstat -CS`

- 仅显示 Internet 套接字，如果本地和远程地址不在环回网络前缀 127.0.0.0/8 中，或不包含 IPv6 环回地址 ::1：

`sockstat -L`

- 不显示表头（静默模式），显示 [u]nix 套接字并显示 `inp_gencnt`：

`sockstat -qui`