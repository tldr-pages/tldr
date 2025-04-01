# caddy

> 一款用 Go 编写的，支持自动 HTTPS 的企业级开源Web服务器。
> 更多信息：<https://caddyserver.com>.

- 在前台启动 Caddy：

`caddy run`

- 使用指定的 Caddyfile 启动 Caddy：

`caddy run --config {{path/to/Caddyfile}}`

- 在后台启动 Caddy：

`caddy start`

- 停止后台运行的 Caddy 进程：

`caddy stop`

- 在指定端口上运行一个带有可浏览界面的简单文件服务器：

`caddy file-server --listen :{{8000}} --browse`

- 运行一个反向代理服务器：

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`