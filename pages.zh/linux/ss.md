# ss

> 用于调查套接字的工具。
> 更多信息：<https://manned.org/ss.8>。

- 显示所有 TCP/UDP/RAW/UNIX 套接字：

`ss -a {{-t|-u|-w|-x}}`

- 按状态过滤 TCP 套接字，仅显示/排除：

`ss {{state/exclude}} {{bucket/big/connected/synchronized/...}}`

- 显示所有连接到本地 HTTPS 端口 (443) 的 TCP 套接字：

`ss -t src :{{443}}`

- 显示所有在本地 8080 端口上监听的 TCP 套接字：

`ss -lt src :{{8080}}`

- 显示所有连接到远程 SSH 端口的 TCP 套接字及其进程：

`ss -pt dst :{{ssh}}`

- 显示在特定源和目标端口上连接的所有 UDP 套接字：

`ss -u 'sport == :{{source_port}} and dport == :{{destination_port}}'`

- 显示在子网 192.168.0.0/16 上本地连接的所有 TCP IPv4 套接字：

`ss -4t src {{192.168/16}}`

- 杀死目标 IP 为 192.168.1.17、目标端口为 8080 的 IPv4 或 IPv6 套接字连接：

`ss --kill dst {{192.168.1.17}} dport = {{8080}}`