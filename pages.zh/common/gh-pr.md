# gh pr

> 管理 GitHub 拉取请求。
> 一些子命令（例如 `create`）有自己的使用文档。
> 更多信息：<https://cli.github.com/manual/gh_pr>。

- 创建一个拉取请求：

`gh pr {{[new|create]}}`

- 在本地检出指定的拉取请求：

`gh {{[co|pr checkout]}} {{pr_号|url|分支}}`

- 查看当前分支上拉取请求所做的更改：

`gh pr diff`

- 批准当前分支关联的拉取请求：

`gh pr review {{[-a|--approve]}}`

- 以交互式方式合并当前分支关联的拉取请求：

`gh pr merge`

- 以交互式方式编辑拉取请求：

`gh pr edit`

- 修改拉取请求的目标分支：

`gh pr edit {{[-B|--base]}} {{分支名}}`

- 查看当前仓库中拉取请求的状态：

`gh pr status`
