# atuin

> 将您的 shell 历史记录存储在可搜索的数据库中。
> 可选择在不同机器之间同步您的加密历史记录。
> 更多信息：<https://atuin.sh/docs/commands>。

- 将 atuin 安装到您的 shell 中：

`eval "$(atuin init {{bash|zsh|fish}})"`

- 从 shell 默认历史文件导入历史记录：

`atuin import auto`

- 在 shell 历史中搜索特定命令：

`atuin search {{command}}`

- 使用指定的 [u] 用户名、[e] 邮箱和 [p] 密码在默认同步服务器上注册一个账户：

`atuin register -u {{username}} -e {{email}} -p {{password}}`

- 登录到默认同步服务器：

`atuin login -u {{username}} -p {{password}}`

- 与同步服务器同步历史记录：

`atuin sync`