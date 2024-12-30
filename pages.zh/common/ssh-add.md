# ssh-add

> 管理加载的 SSH 密钥在 `ssh-agent` 中。
> 确保 `ssh-agent` 正在运行，以便密钥能够被加载。
> 更多信息：<https://man.openbsd.org/ssh-add>。

- 将默认 SSH 密钥添加到 `~/.ssh` 的 ssh-agent 中：

`ssh-add`

- 将特定密钥添加到 ssh-agent：

`ssh-add {{path/to/private_key}}`

- 列出当前加载的密钥的指纹：

`ssh-add -l`

- 从 ssh-agent 中删除密钥：

`ssh-add -d {{path/to/private_key}}`

- 从 ssh-agent 中删除所有当前加载的密钥：

`ssh-add -D`

- 将密钥添加到 ssh-agent 和钥匙串中：

`ssh-add -K {{path/to/private_key}}`