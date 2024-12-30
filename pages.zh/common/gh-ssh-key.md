# gh ssh-key

> 管理 GitHub SSH 密钥。
> 更多信息：<https://cli.github.com/manual/gh_ssh-key>。

- 显示帮助：

`gh ssh-key`

- 列出当前认证用户的 SSH 密钥：

`gh ssh-key list`

- 将 SSH 密钥添加到当前认证用户的账户：

`gh ssh-key add {{path/to/key.pub}}`

- 将带有特定标题的 SSH 密钥添加到当前认证用户的账户：

`gh ssh-key add --title {{title}} {{path/to/key.pub}}`