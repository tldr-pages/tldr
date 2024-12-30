# tailscale up

> 将客户端连接到 Tailscale 网络。
> 在 1.8 及以上版本中，命令行参数会被存储并重用，直到它们被覆盖或调用 `--reset`。
> 更多信息：<https://tailscale.com/kb/1080/cli/#up>。

- 连接到 Tailscale：

`sudo tailscale up`

- 连接并将当前机器作为互联网流量的出口节点：

`sudo tailscale up --advertise-exit-node`

- 使用特定节点进行互联网流量连接：

`sudo tailscale up --exit-node={{exit_node_ip}}`

- 连接并阻止对当前节点的传入连接：

`sudo tailscale up --shields-up`

- 连接并不接受来自管理面板的 DNS 配置（默认值为 `true`）：

`sudo tailscale up --accept-dns=false`

- 连接并将 Tailscale 配置为子网路由器：

`sudo tailscale up --advertise-routes={{10.0.0.0/24,10.0.1.0/24,...}}`

- 连接并接受来自 Tailscale 的子网路由：

`sudo tailscale up --accept-routes`

- 重置未指定的设置为默认值并连接：

`sudo tailscale up --reset`