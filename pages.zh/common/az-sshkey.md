# az sshkey

> 管理虚拟机的 SSH 公钥。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/sshkey>。

- 创建一个新的 SSH 密钥：

`az sshkey create --name {{name}} --resource-group {{resource_group}}`

- 上传一个现有的 SSH 密钥：

`az sshkey create --name {{name}} --resource-group {{resource_group}} --public-key "{{@path/to/key.pub}}"`

- 列出所有 SSH 公钥：

`az sshkey list`

- 显示有关 SSH 公钥的信息：

`az sshkey show --name {{name}} --resource-group {{resource_group}}`