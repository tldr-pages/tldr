# ss

> 用于检查套接字（sockets）的实用程序。
> 更多信息：<https://manned.org/ss>。

- 显示所有 TCP/UDP/RAW/UNIX 套接字：

`ss --all {{--tcp|--udp|--raw|--unix}}`

- 根据状态过滤 TCP 套接字（仅显示/排除）：

`ss {{state|exclude}} {{bucket|big|connected|synchronized|...}}`

- 显示所有连接到本地 HTTPS 端口（443）的 TCP 套接字：

`ss --tcp src :{{443}}`

- 显示所有监听本地 8080 端口的 TCP 套接字：

`ss --listening --tcp src :{{8080}}`

- 显示所有连接到远程 SSH 端口的 TCP 套接字及其对应的进程：

`ss --processes --tcp dst :{{ssh}}`

- 显示连接到特定源端口和目的端口的所有 UDP 套接字：

`ss --udp 'sport == :{{source_port}} and dport == :{{destination_port}}'`

- 显示在 192.168.0.0/16 子网上本地连接的所有 TCP IPv4 套接字：

`ss --ipv4 --tcp src {{192.168/16}}`

- 断开（Kill）具有特定目的 IP 和端口的 IPv4 或 IPv6 套接字连接：

`ss --kill dst {{ip_address}} dport = {{port}}`
