# glab 仓库

> 与 GitLab 仓库进行工作。
> 更多信息：<https://glab.readthedocs.io/en/latest/repo/index.html#synopsis>。

- 创建一个新仓库（如果未设置仓库名称，则默认名称将为当前目录的名称）：

`glab repo create {{name}}`

- 克隆一个仓库：

`glab repo clone {{owner}}/{{repository}}`

- 派生并克隆一个仓库：

`glab repo fork {{owner}}/{{repository}} --clone`

- 在默认网页浏览器中查看仓库：

`glab repo view {{owner}}/{{repository}} --web`

- 在 GitLab 实例中搜索一些仓库：

`glab repo search -s {{search_string}}`