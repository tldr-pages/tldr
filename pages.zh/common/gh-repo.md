# gh repo

> 在命令行上操作 GitHub 仓库。
> 更多信息：<https://cli.github.com/manual/gh_repo>.

- 创建一个新的仓库（如果没有设置仓库名称，默认将为当前目录的名称）：

`gh repo create {{名称}}`

- 克隆一个仓库：

`gh repo clone {{拥有者}}/{{仓库}}`

- 复刻并克隆一个仓库：

`gh repo fork {{拥有者}}/{{仓库}} --clone`

- 在默认的网络浏览器中查看一个仓库：

`gh repo view {{仓库}} --web`

- 列出特定用户或组织拥有的仓库（如果未设置拥有者，默认拥有者将是当前登录用户）：

`gh repo list {{拥有者}}`

- 仅列出非派生的仓库，并限制列出的仓库数量（默认：30）：

`gh repo list {{拥有者}} --source -L {{限制数量}}`

- 列出具有特定主要编程语言的仓库：

`gh repo list {{拥有者}} --language {{语言名称}}`
