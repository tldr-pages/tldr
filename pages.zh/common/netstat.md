# netstat

> 显示与网络相关的信息，例如打开的连接、打开的套接字端口等。
> 另见：`ss`。
> 更多信息：<https://manned.org/netstat>。

- 列出所有端口：

`netstat --all`

- 列出所有监听端口：

`netstat --listening`

- 列出监听的TCP端口：

`netstat --tcp`

- 显示PID和程序名称：

`netstat --program`

- 持续列出信息：

`netstat --continuous`

- 列出路由，并不将IP地址解析为主机名：

`netstat --route --numeric`

- 列出监听的TCP和UDP端口（如果你是root用户，还包括用户和进程）：

`netstat --listening --program --numeric --tcp --udp --extend`