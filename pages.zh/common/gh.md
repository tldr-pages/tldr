# gh

> 与 GitHub 无缝协作。
> 一些子命令如 `config` 有自己的使用文档。
> 更多信息：<https://cli.github.com/>.

- 本地克隆一个 GitHub 仓库：

`gh repo clone {{owner}}/{{repository}}`

- 创建一个新问题：

`gh issue create`

- 查看和筛选当前仓库的开放问题：

`gh issue list`

- 在默认网页浏览器中查看一个问题：

`gh issue view --web {{issue_number}}`

- 创建一个拉取请求：

`gh pr create`

- 在默认网页浏览器中查看一个拉取请求：

`gh pr view --web {{pr_number}}`

- 在本地检出一个特定的拉取请求：

`gh pr checkout {{pr_number}}`

- 检查一个仓库的拉取请求状态：

`gh pr status`