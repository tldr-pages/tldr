# netstat

> 显示活动的 TCP 连接、计算机正在监听的端口、网络适配器统计信息、IP 路由表、IPv4 统计信息和 IPv6 统计信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/netstat>。

- 显示活动的 TCP 连接：

`netstat`

- 显示所有活动的 TCP 连接以及计算机正在监听的 TCP 和 UDP 端口：

`netstat -a`

- 显示网络适配器统计信息，如发送和接收的字节数和数据包数：

`netstat -e`

- 显示活动的 TCP 连接，并以数字形式显示地址和端口号：

`netstat -n`

- 显示活动的 TCP 连接，并包含每个连接的进程 ID (PID)：

`netstat -o`

- 显示 IP 路由表的内容：

`netstat -r`

- 按协议显示统计信息：

`netstat -s`

- 显示当前打开的端口及其相关 IP 地址列表：

`netstat -an`
