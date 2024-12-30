# sockstat

> 列出打开的互联网或UNIX域套接字。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?sockstat>。

- 查看哪些用户/进程在监听哪些端口：

`sockstat -l`

- 显示使用特定协议在特定端口上监听的IPv[4]/IPv[6]套接字的信息：

`sockstat -{{4|6}} -l -P {{tcp|udp|sctp|divert}} -p {{port1,port2...}}`

- 还显示已连接的套接字，不将数字UID解析为用户名，并使用更宽的字段大小：

`sockstat -cnw`

- 仅显示属于特定监狱ID或名称的套接字，并以详细模式显示：

`sockstat -jv`

- 显示协议状态和远程UDP封装端口号（如果适用）（目前仅为SCTP和TCP实现）：

`sockstat -sU`

- 显示拥塞控制模块和协议栈（如果适用）（目前仅为TCP实现）：

`sockstat -CS`

- 仅显示互联网套接字，如果本地和外国地址不在回环网络前缀127.0.0.0/8中，或不包含IPv6回环地址::1：

`sockstat -L`

- 不显示头部（静默模式），显示UNIX套接字并显示`inp_gencnt`：

`sockstat -qui`