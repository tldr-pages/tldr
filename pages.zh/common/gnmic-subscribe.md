# gnmic 订阅

> 订阅 gnmic 网络设备状态更新。
> 更多信息：<https://gnmic.kmrd.dev/cmd/subscribe>。

- 在特定路径的子树下订阅目标状态更新：

`gnmic --address {{ip:port}} subscribe --path {{path}}`

- 以 30 秒的采样间隔订阅目标（默认为 10 秒）：

`gnmic -a {{ip:port}} subscribe --path {{path}} --sample-interval 30s`

- 以采样间隔和仅在变化时更新的方式订阅目标：

`gnmic -a {{ip:port}} subscribe --path {{path}} --stream-mode on-change --heartbeat-interval 1m`

- 仅订阅目标的一个更新：

`gnmic -a {{ip:port}} subscribe --path {{path}} --mode once`

- 订阅目标并指定响应编码（json_ietf）：

`gnmic -a {{ip:port}} subscribe --path {{path}} --encoding json_ietf`