# glab repo

> 管理 GitLab 仓库。
> 更多信息：<https://glab.readthedocs.io/en/latest/repo/index.html#synopsis>。

- 创建一个新仓库（如果未设置仓库名称，默认名称为当前目录的名称）：

`glab repo create {{name}}`

- 克隆一个仓库：

`glab repo clone {{owner}}/{{repository}}`

- 叉克隆一个仓库：

`glab repo fork {{owner}}/{{repository}} --clone`

- 在默认网页浏览器中查看仓库：

`glab repo view {{owner}}/{{repository}} --web`

- 在 GitLab 实例中搜索仓库：

`glab repo search -s {{search_string}}`