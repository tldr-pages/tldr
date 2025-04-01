# tailscale up

> 将客户端连接到 Tailscale 网络。
> 注意：运行 `sudo tailscale set --operator $USER` 以允许当前用户执行这些命令。
> 所有在此描述的选项都可以通过 `tailscale set --option argument` 在稍后进行更改。使用 `--option=false` 来禁用不需要参数的选项。
> 更多信息：<https://tailscale.com/kb/1080/cli/#up>。

- 连接到 Tailscale：

`tailscale up`

- 连接并提供当前机器作为互联网流量的出口节点：

`tailscale up --advertise-exit-node`

- 使用特定节点连接互联网流量：

`tailscale up --exit-node {{exit_node_ip}}`

- 连接并阻止向当前节点发起的入站连接：

`tailscale up --shields-up`

- 连接并禁止从管理面板接受 DNS 配置（默认为 `true`）：

`tailscale up --accept-dns=false`

- 连接并配置 Tailscale 作为子网路由器：

`tailscale up --advertise-routes {{10.0.0.0/24,10.0.1.0/24,...}}`

- 连接并接受来自 Tailscale 的子网路由：

`tailscale up --accept-routes`

- 重置未指定的设置为默认值并连接：

`tailscale up --reset`