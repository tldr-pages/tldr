# gh alias

> 管理 GitHub CLI 命令别名。
> 更多信息：<https://cli.github.com/manual/gh_alias>.

- 列出所有配置的 `gh` 别名：

`gh alias list`

- 创建 `gh` 子命令别名：

`gh alias set {{pv}} '{{pr view}}'`

- 将 shell 命令设置为 `gh` 子命令：

`gh alias set --shell {{alias_name}} {{command}}`

- 删除命令快捷方式：

`gh alias delete {{alias_name}}`

- 显示子命令帮助：

`gh alias`