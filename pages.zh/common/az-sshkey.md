# az sshkey

> 管理与虚拟机关联的 SSH 公钥。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/sshkey>。

- 创建新的 SSH 密钥：

`az sshkey create --name {{name}} --resource-group {{resource_group}}`

- 上传现有 SSH 密钥：

`az sshkey create --name {{name}} --resource-group {{resource_group}} --public-key "{{@path/to/key.pub}}"`

- 列出所有 SSH 公钥：

`az sshkey list`

- 显示关于 SSH 公钥的信息：

`az sshkey show --name {{name}} --resource-group {{resource_group}}`
