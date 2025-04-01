# gh extension

> 管理 GitHub CLI 的扩展。
> 更多信息：<https://cli.github.com/manual/gh_extension>.

- 在同名目录中初始化一个新的 GitHub CLI 扩展项目：

`gh extension create {{extension_name}}`

- 从 GitHub 仓库安装扩展：

`gh extension install {{owner}}/{{repository}}`

- 列出已安装的扩展：

`gh extension list`

- 升级特定的扩展：

`gh extension upgrade {{extension_name}}`

- 升级所有扩展：

`gh extension upgrade --all`

- 列出已安装的扩展：

`gh extension list`

- 移除扩展：

`gh extension remove {{extension_name}}`

- 显示子命令的帮助信息：

`gh extension {{subcommand}} --help`