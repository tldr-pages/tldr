# warp-cli

> 连接、断开和切换与 Cloudflare 的 WARP 服务的连接模式。
> WARP 是一种 VPN，旨在保护隐私、安全性和速度。
> 另请参见：`fastd`、`ivpn`、`mozillavpn`、`mullvad`。
> 更多信息请访问：<https://developers.cloudflare.com/warp-client/>。

- 注册当前设备到 WARP（必须在第一次连接之前运行）：

`warp-cli registration new`

- 连接到 WARP：

`warp-cli connect`

- 断开与 WARP 的连接：

`warp-cli disconnect`

- 显示 WARP 连接状态：

`warp-cli status`

- 切换到特定模式：

`warp-cli set-mode {{mode}}`

- 显示帮助信息：

`warp-cli help`

- 显示子命令的帮助信息：

`warp-cli help {{subcommand}}`