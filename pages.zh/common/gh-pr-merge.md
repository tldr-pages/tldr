# gh pr merge

> 合并 GitHub 拉取请求。
> 更多信息：<https://cli.github.com/manual/gh_pr_merge>。

- 以交互式方式合并当前分支关联的拉取请求：

`gh pr merge`

- 合并当前分支到指定的拉取请求：

`gh pr merge {{pr_号}} {{[-m|--merge]}}`

- 压缩合并拉取请求，并删除该分支：

`gh pr merge {{pr_号}} {{[-sd|--squash --delete-branch]}}`

- 变基合并拉取请求：

`gh pr merge {{pr_号}} {{[-r|--rebase]}}`

- 开启自动合并（压缩合并）：

`gh pr merge {{pr_号}} --auto {{[-s|--squash]}}`

- 使用管理员权限合并（如果允许）：

`gh pr merge {{pr_号}} --admin`
