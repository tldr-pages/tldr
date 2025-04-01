# ss

> 用于调查套接字的工具。
> 更多信息：<https://manned.org/ss.8>.

- 显示所有 TCP/UDP/RAW/UNIX 套接字：

`ss {{[-a|--all]}} {{-t|-u|-w|-x}}`

- 按状态过滤 TCP 套接字，仅包括/排除：

`ss {{state|exclude}} {{bucket|big|connected|synchronized|...}}`

- 显示所有连接到本地 HTTPS 端口（443）的 TCP 套接字：

`ss {{[-t|--tcp]}} src :{{443}}`

- 显示所有在本地 8080 端口监听的 TCP 套接字：

`ss {{[-lt|--listening --tcp]}} src :{{8080}}`

- 显示所有连接到远程 SSH 端口的 TCP 套接字及其关联的进程：

`ss {{[-pt|--processes --tcp]}} dst :{{ssh}}`

- 显示所有在特定源端口和目标端口上连接的 UDP 套接字：

`ss {{[-u|--udp]}} 'sport == :{{source_port}} and dport == :{{destination_port}}'`

- 显示所有在本地连接到 192.168.0.0/16 子网的 TCP IPv4 套接字：

`ss {{[-4t|--ipv4 --tcp]}} src {{192.168/16}}`

- 终止目标 IP 192.168.1.17 和目标端口 8080 的 IPv4 或 IPv6 套接字连接：

`ss {{[-K|--kill]}} dst {{192.168.1.17}} dport = {{8080}}`
