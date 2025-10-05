# atuin

> 存储您的 shell 历史记录到可搜索的数据库。
> 可选择在机器之间同步加密历史记录。
> 更多信息：<https://docs.atuin.sh/>.

- 安装 atuin 到您的 shell:

`eval "$(atuin init {{bash|zsh|fish}})"`

- 从 shell 默认历史记录文件导入：

`atuin import auto`

- 搜索 shell 历史记录中指定的命令：

`atuin search {{命令}}`

- 使用指定的用户名，邮箱和密码在默认同步服务器注册账号：

`atuin register -u {{用户名}} -e {{邮箱}} -p {{密码}}`

- 登录默认同步服务器：

`atuin login -u {{用户名}} -p {{密码}}`

- 与同步服务器同步历史记录：

`atuin sync`
