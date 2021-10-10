# netstat

> 显示与网络相关的信息，如打开的连接、打开的套接字端口等。
> 更多信息：<https://man7.org/linux/man-pages/man8/netstat.8.html>.

- 列出所有端口：

`netstat -a`

- 列出所有被侦听端口：

`netstat -l`

- 列出侦听的 TCP 端口：

`netstat -t`

- 显示监听给定协议监听的 PID 和程序名：

`netstat -p {{协议}}`

- 打印路由表：

`netstat -nr`
