# glab

> 与GitLab无缝协作。
> 一些子命令如 `config` 有自己的使用文档。
> 更多信息：<https://github.com/profclems/glab>。

- 在本地克隆一个GitLab仓库：

`glab repo clone {{owner}}/{{repository}}`

- 创建一个新问题：

`glab issue create`

- 查看和过滤当前仓库的开放问题：

`glab issue list`

- 在默认浏览器中查看一个问题：

`glab issue view --web {{issue_number}}`

- 创建一个合并请求：

`glab mr create`

- 在默认网页浏览器中查看一个拉取请求：

`glab mr view --web {{pr_number}}`

- 在本地检出一个特定的拉取请求：

`glab mr checkout {{pr_number}}`