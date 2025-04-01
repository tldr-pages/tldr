# gnmic

> 一个 gNMI 命令行客户端。
> 管理 gNMI 网络设备配置并查看操作数据。
> 更多信息：<https://gnmic.kmrd.dev>。

- 请求设备功能：

`gnmic --address {{ip:port}} capabilities`

- 提供用户名和密码以获取设备功能：

`gnmic --address {{ip:port}} --username {{username}} --password {{password}} capabilities`

- 获取指定路径下设备状态的快照：

`gnmic -a {{ip:port}} get --path {{path}}`

- 更新指定路径下的设备状态：

`gnmic -a {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- 订阅指定路径下子树的状态更新：

`gnmic -a {{ip:port}} subscribe --path {{path}}`