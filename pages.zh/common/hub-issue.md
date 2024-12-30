# hub 问题

> 管理 Github 问题。
> 更多信息：<https://hub.github.com/hub-issue.1.html>。

- 列出最后 10 个带有 `bug` 标签的问题：

`hub issue list --limit {{10}} --labels "{{bug}}"`

- 显示特定的问题：

`hub issue show {{issue_number}}`

- 列出 10 个已关闭的问题，指定给特定用户：

`hub issue --state {{closed}} --assignee {{username}} --limit {{10}}`