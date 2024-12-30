# git reflog

> 显示对本地引用（如 HEAD、分支或标签）所做更改的日志。
> 更多信息：<https://git-scm.com/docs/git-reflog>。

- 显示 HEAD 的 reflog：

`git reflog`

- 显示给定分支的 reflog：

`git reflog {{branch_name}}`

- 仅显示 reflog 中的 5 条最新条目：

`git reflog {{-n|--max-count}} 5`