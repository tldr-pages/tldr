# chisel

> 创建通过 HTTP 传输、通过 SSH 保护的 TCP/UDP 隧道。
> 包括客户端和服务器在同一个 `chisel` 可执行文件中。
> 更多信息：<https://github.com/jpillora/chisel>。

- 运行 Chisel 服务器：

`chisel server`

- 运行监听特定端口的 Chisel 服务器：

`chisel server -p {{server_port}}`

- 运行一个接受使用用户名和密码进行身份验证的 Chisel 服务器：

`chisel server --auth {{username}}:{{password}}`

- 连接到 Chisel 服务器并将特定端口隧道到远程服务器和端口：

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- 连接到 Chisel 服务器并将特定主机和端口隧道到远程服务器和端口：

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- 使用用户名和密码身份验证连接到 Chisel 服务器：

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- 在特定端口上以反向模式初始化 Chisel 服务器，同时启用 SOCKS5 代理（在 1080 端口）功能：

`chisel server -p {{server_port}} --reverse --socks5`

- 连接到特定 IP 和端口的 Chisel 服务器，创建一个映射到本地 SOCKS 代理的反向隧道：

`chisel client {{server_ip}}:{{server_port}} R:socks`