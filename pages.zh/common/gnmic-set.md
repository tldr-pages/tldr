# gnmic set

> 修改 gnmi 网络设备配置。
> 更多信息：<https://gnmic.kmrd.dev/cmd/set>。

- 更新路径的值：

`gnmic --address {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- 更新路径的值以匹配 JSON 文件的内容：

`gnmic -a {{ip:port}} set --update-path {{path}} --update-file {{filepath}}`

- 替换路径的值以匹配 JSON 文件的内容：

`gnmic -a {{ip:port}} set --replace-path {{path}} --replace-file {{filepath}}`

- 删除指定路径的节点：

`gnmic -a {{ip:port}} set --delete {{path}}`