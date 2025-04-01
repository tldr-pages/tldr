# cockpit-ws

> 在浏览器应用程序与各种配置工具和服务（如 `cockpit-bridge`）之间进行通信。
> 更多信息：<https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- 通过 SSH 在 `127.0.0.1` 启动，端口 `22` 已启用：

`cockpit-ws --local-ssh`

- 在特定端口上启动 HTTP 服务器：

`cockpit-ws --port {{port}}`

- 启动并绑定到特定 IP 地址（默认为 `0.0.0.0`）：

`cockpit-ws --address {{ip_address}}`

- 启动时不使用 TLS：

`cockpit-ws --no-tls`

- 显示帮助信息：

`cockpit-ws --help`
