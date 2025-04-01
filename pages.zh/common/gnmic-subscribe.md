# gnmic subscribe

> 订阅 gnmic 网络设备状态更新。
> 更多信息：<https://gnmic.kmrd.dev/cmd/subscribe>。

- 订阅目标在特定路径子树下的状态更新：

`gnmic --address {{ip:port}} subscribe --path {{path}}`

- 订阅目标，采样间隔为 30 秒（默认为 10 秒）：

`gnmic -a {{ip:port}} subscribe --path {{path}} --sample-interval 30s`

- 订阅目标，带有采样间隔且仅在状态变化时更新：

`gnmic -a {{ip:port}} subscribe --path {{path}} --stream-mode on-change --heartbeat-interval 1m`

- 订阅目标仅获取一次更新：

`gnmic -a {{ip:port}} subscribe --path {{path}} --mode once`

- 订阅目标并指定响应编码（json_ietf）：

`gnmic -a {{ip:port}} subscribe --path {{path}} --encoding json_ietf`