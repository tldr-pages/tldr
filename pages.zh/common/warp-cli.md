# warp-cli

> 连接到 Cloudflare 的 WARP 服务，断开连接或切换连接模式。
> WARP 是一个可以为流量加密以增强隐私、安全性和速度的 VPN。
> 参见：`fastd`、`ivpn`、`mozillavpn`、`mullvad`。
> 更多信息：<https://developers.cloudflare.com/warp-client/>.

- 注册当前设备到 WARP（首次连接前必须运行此命令）：

`warp-cli registration new`

- 连接到 WARP：

`warp-cli connect`

- 从 WARP 断开连接：

`warp-cli disconnect`

- 显示 WARP 连接状态：

`warp-cli status`

- 切换到特定模式：

`warp-cli set-mode {{mode}}`

- 显示帮助信息：

`warp-cli help`

- 显示子命令的帮助信息：

`warp-cli help {{subcommand}}`
