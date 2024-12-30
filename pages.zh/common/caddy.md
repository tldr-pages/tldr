# Caddy

> 一个企业级开源 web 服务器，具有自动 HTTPS，使用 Go 语言编写。
> 更多信息请访问：<https://caddyserver.com>。

- 在前台启动 Caddy：

`caddy run`

- 使用指定的 Caddyfile 启动 Caddy：

`caddy run --config {{path/to/Caddyfile}}`

- 在后台启动 Caddy：

`caddy start`

- 停止后台的 Caddy 进程：

`caddy stop`

- 在指定端口上运行一个简单的文件服务器，并提供可浏览的界面：

`caddy file-server --listen :{{8000}} --browse`

- 运行一个反向代理服务器：

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`