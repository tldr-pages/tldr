# glab alias

> 管理 GitLab CLI 命令别名。
> 更多信息：<https://glab.readthedocs.io/en/latest/alias>。

- 显示子命令帮助：

`glab alias`

- 列出 `glab` 配置的所有别名：

`glab alias list`

- 创建 `glab` 子命令别名：

`glab alias set {{mrv}} '{{mr view}}'`

- 将 shell 命令设置为 `glab` 子命令：

`glab alias set --shell {{alias_name}} {{command}}`

- 删除命令快捷方式：

`glab alias delete {{alias_name}}`
