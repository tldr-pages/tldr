# tailscale

> 一个私有的 WireGuard 网络服务。
> 一些子命令例如 `up` 有其自己的使用文档。
> 更多信息：<https://tailscale.com>。

- 连接到 Tailscale：

`sudo tailscale up`

- 从 Tailscale 断开连接：

`sudo tailscale down`

- 显示当前的 Tailscale IP 地址：

`tailscale ip`

- 在 Tailscale 层上 ping 一个对等节点，并显示每个响应所采取的路由：

`tailscale ping {{ip|hostname}}`

- 分析本地网络状况并显示结果：

`tailscale netcheck`

- 启动一个 web 服务器以控制 Tailscale：

`tailscale web`

- 显示一个可共享的标识符以帮助诊断问题：

`tailscale bugreport`

- 显示子命令的帮助信息：

`tailscale {{subcommand}} --help`