# vcsh

> 使用 Git 仓库的主目录版本控制系统。
> 另见：`chezmoi`、`stow`、`tuckr`、`homeshick`。
> 更多信息：<https://github.com/RichiH/vcsh>。

- 初始化一个（空的）仓库：

`vcsh init {{repository_name}}`

- 将仓库克隆到自定义目录名称：

`vcsh clone {{git_url}} {{repository_name}}`

- 列出所有受管理的仓库：

`vcsh list`

- 在受管理的仓库上执行 Git 命令：

`vcsh {{repository_name}} {{git_command}}`

- 将所有受管理的仓库推送到/从远程拉取：

`vcsh {{push|pull}}`

- 为受管理的仓库编写自定义的 `.gitignore` 文件：

`vcsh write-gitignore {{repository_name}}`