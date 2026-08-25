# gh pr checks

> 查看 GitHub 拉取请求的 CI 状态检查结果。
> 更多信息：<https://cli.github.com/manual/gh_pr_checks>。

- 显示当前分支关联的拉取请求的状态检查结果：

`gh pr checks`

- 显示指定拉取请求的状态检查结果：

`gh pr checks {{pr_号}}`

- 实时监控状态检查，直到全部完成：

`gh pr checks {{pr_号}} --watch`

- 仅显示强制要求的检查结果：

`gh pr checks {{pr_号}} --required`
