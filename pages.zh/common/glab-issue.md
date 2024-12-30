# glab 问题

> 管理 GitLab 问题。
> 更多信息：<https://glab.readthedocs.io/en/latest/issue>。

- 显示特定问题：

`glab issue view {{issue_number}}`

- 在默认网页浏览器中显示特定问题：

`glab issue view {{issue_number}} --web`

- 在默认网页浏览器中创建新问题：

`glab issue create --web`

- 列出最近 10 个带有 `bug` 标签的问题：

`glab issue list --per-page {{10}} --label "{{bug}}"`

- 列出由特定用户创建的已关闭问题：

`glab issue list --closed --author {{username}}`

- 重新打开特定问题：

`glab issue reopen {{issue_number}}`