# gnmic

> 一个 gNMI 命令行客户端。
> 管理 gNMI 网络设备配置并查看操作数据。
> 更多信息：<https://gnmic.kmrd.dev>。

- 请求设备能力：

`gnmic --address {{ip:port}} capabilities`

- 提供用户名和密码以获取设备能力：

`gnmic --address {{ip:port}} --username {{username}} --password {{password}} capabilities`

- 获取特定路径下设备状态的快照：

`gnmic -a {{ip:port}} get --path {{path}}`

- 更新特定路径下的设备状态：

`gnmic -a {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- 订阅特定路径下子树的目标状态更新：

`gnmic -a {{ip:port}} subscribe --path {{path}}`