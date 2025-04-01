# vcsh

> 使用 Git 仓库管理家目录的版本控制系统。
> 参见：`chezmoi`，`stow`，`tuckr`，`homeshick`。
> 更多信息：<https://github.com/RichiH/vcsh>。

- 初始化一个（空的）仓库：

`vcsh init {{repository_name}}`

- 将仓库克隆到自定义目录名称中：

`vcsh clone {{git_url}} {{repository_name}}`

- 列出所有管理的仓库：

`vcsh list`

- 在管理的仓库上执行 Git 命令：

`vcsh {{repository_name}} {{git_command}}`

- 将所有管理的仓库推送到或从远程仓库拉取：

`vcsh {{push|pull}}`

- 为管理的仓库编写自定义的 `.gitignore` 文件：

`vcsh write-gitignore {{repository_name}}`