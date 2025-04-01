# gh pr merge

> 合并 GitHub 拉取请求。
> 更多信息： <https://cli.github.com/manual/gh_pr_merge>.

- 交互式合并与当前分支关联的拉取请求：

`gh pr merge`

- 交互式合并指定的拉取请求：

`gh pr merge {{pr_number}}`

- 合并拉取请求，同时在本地和远程删除分支：

`gh pr merge --delete-branch`

- 使用指定的合并策略合并当前拉取请求：

`gh pr merge --{{merge|squash|rebase}}`

- 使用指定的合并策略和提交信息合并当前拉取请求：

`gh pr merge --{{merge|squash|rebase}} --subject {{commit_message}}`

- 将当前拉取请求压缩为一个带有消息正文的提交并合并：

`gh pr merge --squash --body="{{commit_message_body}}"`

- 显示帮助：

`gh pr merge --help`
