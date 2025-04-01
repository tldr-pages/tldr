# tailscale

> 私有 WireGuard 网络服务。
> 一些子命令（如 `up`）有自己的使用文档。
> 更多信息：<https://tailscale.com/kb/1080/cli>.

- 允许当前用户操作 Tailscale 守护进程：

`sudo tailscale set --operator $USER`

- 连接到 Tailscale：

`tailscale up`

- 从 Tailscale 断开连接：

`tailscale down`

- 显示连接到 Tailscale 的所有设备（包括它们的 IP 地址）：

`tailscale status`

- 在 Tailscale 层ping一个对等节点，并显示每次响应所经过的路由：

`tailscale ping {{ip|hostname}}`

- 分析本地网络状况并显示结果：

`tailscale netcheck`

- 启动一个用于控制 Tailscale 守护进程的 Web 服务器：

`tailscale web`

- 显示可共享的标识符以帮助诊断问题：

`tailscale bugreport`
