# netstat

> 显示与网络相关的信息，如打开的连接、打开的套接字端口等.

- 列出所有端口:

`netstat -a`

- 列出所有被侦听端口:

`netstat -l`

- 列出侦听的 TCP 端口:

`netstat -t`

- 显示监听给定协议监听的 PID 和程序名:

`netstat -p {{协议}}`

- 连续列出信息（这条我电脑里 netstat 是不支持的。谁明白麻烦提交 pr!):

`netstat -c`

- 打印路由表:

`netstat -nr`
