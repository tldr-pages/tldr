# gh repo

> 与 GitHub 存储库进行交互。
> 更多信息：<https://cli.github.com/manual/gh_repo>。

- 创建一个新的存储库（如果未设置存储库名称，则默认名称将为当前目录的名称）：

`gh repo create {{name}}`

- 克隆一个存储库：

`gh repo clone {{owner}}/{{repository}}`

- 派生并克隆一个存储库：

`gh repo fork {{owner}}/{{repository}} --clone`

- 在默认网页浏览器中查看一个存储库：

`gh repo view {{repository}} --web`

- 列出特定用户或组织拥有的存储库（如果未设置所有者，则默认所有者为当前登录用户）：

`gh repo list {{owner}}`

- 仅列出非派生的存储库，并限制列出的存储库数量（默认：30）：

`gh repo list {{owner}} --source -L {{limit}}`

- 列出使用特定主编程语言的存储库：

`gh repo list {{owner}} --language {{language_name}}`