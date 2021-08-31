# gh repo

> 在命令行上操作 GitHub 仓库。
> 更多信息：<https://cli.github.com/manual/gh_repo>.

- 创建一个新的仓库（如果没有设置仓库名称，默认将为当前目录的名称）：

`gh repo create {{名称}}`

- 克隆一个仓库：

`gh repo clone {{拥有者}}/{{仓库}}`

- 复刻并克隆一个仓库：

`gh repo fork {{拥有者}}/{{仓库}} --clone`

- 在网络浏览器中查看仓库：

`gh repo view {{仓库}} --web`
