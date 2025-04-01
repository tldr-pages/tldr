# glab issue

> 管理 GitLab 问题。
> 更多信息：<https://glab.readthedocs.io/en/latest/issue>。

- 显示特定问题：

`glab issue view {{issue_number}}`

- 在默认的网络浏览器中显示特定问题：

`glab issue view {{issue_number}} --web`

- 在默认的网络浏览器中创建新问题：

`glab issue create --web`

- 列出带有 `bug` 标签的最后 10 个问题：

`glab issue list --per-page {{10}} --label "{{bug}}"`

- 列出特定用户关闭的问题：

`glab issue list --closed --author {{username}}`

- 重新打开特定问题：

`glab issue reopen {{issue_number}}`