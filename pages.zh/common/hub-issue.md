# hub issue

> 管理 GitHub 问题。
> 更多信息：<https://hub.github.com/hub-issue.1.html>。

- 列出标签为 `bug` 的最后 10 个问题:

`hub issue list --limit {{10}} --labels "{{bug}}"`

- 显示特定问题:

`hub issue show {{issue_number}}`

- 列出分配给特定用户的 10 个已关闭问题:

`hub issue --state {{closed}} --assignee {{username}} --limit {{10}}`