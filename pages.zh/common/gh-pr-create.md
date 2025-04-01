# gh pr create

> 管理 GitHub 拉取请求。
> 更多信息：<https://cli.github.com/manual/gh_pr_create>。

- 交互式创建拉取请求：

`gh pr create`

- 创建拉取请求，从当前分支的提交消息中确定标题和描述：

`gh pr create --fill`

- 创建草稿拉取请求：

`gh pr create --draft`

- 创建拉取请求，指定基础分支、标题和描述：

`gh pr create --base {{base_branch}} --title "{{title}}" --body "{{body}}"`

- 在默认浏览器中打开创建拉取请求的页面：

`gh pr create --web`