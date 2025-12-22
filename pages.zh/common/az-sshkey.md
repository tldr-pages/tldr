# az sshkey

> 使用虚拟机管理 SSH 公钥。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/sshkey>.

- 创建一个新的 SSH 密钥：

`az sshkey create --name {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 上传一个已有的 SSH 密钥：

`az sshkey create --name {{名称}} {{[-g|--resource-group]}} {{资源组}} --public-key "{{@路径/到/key.pub}}"`

- 列出所有 SSH 公钥：

`az sshkey list`

- 显示某个 SSH 公钥的信息：

`az sshkey show --name {{名称}} {{[-g|--resource-group]}} {{资源组}}`
