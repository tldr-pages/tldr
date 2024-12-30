# gnmic 设置

> 修改 gnmi 网络设备配置。
> 更多信息：<https://gnmic.kmrd.dev/cmd/set>。

- 更新路径的值：

`gnmic --address {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- 将路径的值更新为 JSON 文件的内容：

`gnmic -a {{ip:port}} set --update-path {{path}} --update-file {{filepath}}`

- 将路径的值替换为 JSON 文件的内容：

`gnmic -a {{ip:port}} set --replace-path {{path}} --replace-file {{filepath}}`

- 删除给定路径的节点：

`gnmic -a {{ip:port}} set --delete {{path}}`