# gh issue

> 管理 GitHub 问题。
> 更多信息：<https://cli.github.com/manual/gh_issue>.

- 显示特定问题：

`gh issue view {{issue_number}}`

- 在默认的网页浏览器中显示特定问题：

`gh issue view {{issue_number}} --web`

- 在默认的网页浏览器中创建新问题：

`gh issue create --web`

- 列出带有 `bug` 标签的最后 10 个问题：

`gh issue list --limit {{10}} --label "{{bug}}"`

- 列出特定用户创建的已关闭问题：

`gh issue list --state closed --author {{username}}`

- 显示特定仓库中与用户相关的问题状态：

`gh issue status --repo {{owner}}/{{repository}}`

- 重新打开特定问题：

`gh issue reopen {{issue_number}}`
