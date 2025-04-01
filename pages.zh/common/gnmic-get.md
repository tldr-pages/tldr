# gnmic get

> 获取 gnmi 网络设备操作数据的快照。
> 更多信息：<https://gnmic.kmrd.dev/cmd/get>.

- 获取指定路径下的设备状态快照：

`gnmic --address {{ip:port}} get --path {{path}}`

- 查询多个路径下的设备状态：

`gnmic -a {{ip:port}} get --path {{path/to/file_or_directory1}} --path {{path/to/file_or_directory2}}`

- 查询具有共同前缀的多个路径下的设备状态：

`gnmic -a {{ip:port}} get --prefix {{prefix}} --path {{path/to/file_or_directory1}} --path {{path/to/file_or_directory2}}`

- 查询设备状态并指定响应编码（json_ietf）：

`gnmic -a {{ip:port}} get --path {{path}} --encoding json_ietf`