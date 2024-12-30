# gh 代码空间

> 连接和管理您在 GitHub 上的代码空间。
> 更多信息：<https://cli.github.com/manual/gh_codespace>。

- 交互式创建一个 GitHub 代码空间：

`gh codespace create`

- 列出所有可用的代码空间：

`gh codespace list`

- 通过 SSH 交互式连接到一个代码空间：

`gh codespace ssh`

- 交互式传输特定文件到代码空间：

`gh codespace cp {{path/to/source_file}} remote:{{path/to/remote_file}}`

- 交互式列出代码空间的端口：

`gh codespace ports`

- 交互式显示代码空间的日志：

`gh codespace logs`

- 交互式删除一个代码空间：

`gh codespace delete`

- 显示子命令的帮助信息：

`gh codespace {{code|cp|create|delete|edit|...}} --help`