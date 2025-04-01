# brew services

> 使用 `launchctl` 管理 macOS 上的后台服务，或使用 `systemctl` 管理 Linux 上的后台服务。
> 更多信息：<https://docs.brew.sh/Manpage#services-subcommand>.

- 列出当前用户管理的所有服务：

`brew services`

- 列出所有管理服务的详细信息：

`brew services info --all`

- 立即启动服务并注册为登录（或启动）时启动：

`brew services start {{formula}}`

- 立即停止服务并取消注册为登录（或启动）时启动：

`brew services stop {{formula}}`

- 如有必要，先停止然后立即启动服务，并注册为登录（或启动）时启动：

`brew services restart {{formula}}`

- 移除所有未使用的服务：

`brew services cleanup`