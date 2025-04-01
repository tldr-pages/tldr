# gh pr

> 管理 GitHub 拉取请求。
> 一些子命令，如 `create`，有它们自己的使用文档。
> 更多信息：<https://cli.github.com/manual/gh_pr>。

- 创建一个拉取请求：

`gh pr create`

- 本地检出特定的拉取请求：

`gh pr checkout {{pr_number}}`

- 查看当前分支的拉取请求中所做的更改：

`gh pr diff`

- 批准当前分支的拉取请求：

`gh pr review --approve`

- 以交互方式合并与当前分支关联的拉取请求：

`gh pr merge`

- 以交互方式编辑拉取请求：

`gh pr edit`

- 编辑拉取请求的基础分支：

`gh pr edit --base {{branch_name}}`

- 查看当前仓库中拉取请求的状态：

`gh pr status`
