# gh config

> 更改 GitHub CLI 的配置。
> 更多信息：<https://cli.github.com/manual/gh_config>.

- 显示当前使用的 Git 协议：

`gh config get git_protocol`

- 将协议设置为 SSH：

`gh config set git_protocol {{ssh}}`

- 使用 `delta` 以并排模式作为所有 `gh` 命令的默认分页器：

`gh config set pager '{{delta --side-by-side}}'`

- 将文本编辑器设置为 Vim：

`gh config set editor {{vim}}`

- 重置为默认文本编辑器：

`gh config set editor ""`

- 禁用交互式提示：

`gh config set prompt {{disabled}}`

- 设置特定的配置值：

`gh config set {{key}} {{value}}`