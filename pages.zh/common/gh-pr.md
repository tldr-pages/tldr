# gh pr

> 管理 GitHub 拉取请求。
> 某些子命令如 `create` 有自己的使用文档。
> 更多信息：<https://cli.github.com/manual/gh_pr>。

- 创建拉取请求：

`gh pr create`

- 在本地检出特定的拉取请求：

`gh pr checkout {{pr_number}}`

- 查看当前分支拉取请求中的更改：

`gh pr diff`

- 批准当前分支的拉取请求：

`gh pr review --approve`

- 交互式地合并与当前分支关联的拉取请求：

`gh pr merge`

- 交互式地编辑拉取请求：

`gh pr edit`

- 编辑拉取请求的基础分支：

`gh pr edit --base {{branch_name}}`

- 检查当前仓库的拉取请求状态：

`gh pr status`