# gh ssh-key

> 管理 GitHub SSH 密钥。
> 更多信息：<https://cli.github.com/manual/gh_ssh-key>.

- 显示帮助：

`gh ssh-key`

- 列出当前认证用户的所有 SSH 密钥：

`gh ssh-key list`

- 向当前认证用户的账户添加 SSH 密钥：

`gh ssh-key add {{path/to/key.pub}}`

- 带有特定标题向当前认证用户的账户添加 SSH 密钥：

`gh ssh-key add --title {{title}} {{path/to/key.pub}}`
