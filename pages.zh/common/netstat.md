# netstat

> 显示与网络相关的信息，如打开的连接、打开的套接字端口等。
> 另请参阅：`ss`。
> 更多信息：<https://manned.org/netstat>。

- 列出所有端口：

`netstat {{[-a|--all]}}`

- 列出所有被监听端口：

`netstat {{[-l|--listening]}}`

- 列出监听的 TCP 端口：

`netstat {{[-t|--tcp]}}`

- 显示 PID 和程序名：

`netstat {{[-p|--program]}}`

- 持续列出信息：

`netstat {{[-c|--continuous]}}`

- 列出路由并且不解析 IP 到主机名：

`netstat {{[-rn|--route --numeric]}}`

- 列出正在监听的 TCP 和 UDP 端口（如果你是 root 用户，还会显示用户和进程）：

`netstat {{[-tulpne|--tcp --udp --listening --program --numeric --extend]}}`
