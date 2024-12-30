# gh pr merge

> 合并 GitHub 拉取请求。
> 更多信息：<https://cli.github.com/manual/gh_pr_merge>。

- 交互式地合并与当前分支关联的拉取请求：

`gh pr merge`

- 交互式地合并指定的拉取请求：

`gh pr merge {{pr_number}}`

- 合并拉取请求，同时删除本地和远程的分支：

`gh pr merge --delete-branch`

- 使用指定的合并策略合并当前的拉取请求：

`gh pr merge --{{merge|squash|rebase}}`

- 使用指定的合并策略和提交信息合并当前的拉取请求：

`gh pr merge --{{merge|squash|rebase}} --subject {{commit_message}}`

- 将当前的拉取请求压缩成一个提交，并附上消息正文后合并：

`gh pr merge --squash --body="{{commit_message_body}}"`

- 显示帮助信息：

`gh pr merge --help`