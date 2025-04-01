# git reflog

> 显示对本地引用（如 HEAD、分支或标签）更改的日志。
> 更多信息：<https://git-scm.com/docs/git-reflog>.

- 显示 HEAD 的引用日志：

`git reflog`

- 显示指定分支的引用日志：

`git reflog {{branch_name}}`

- 只显示引用日志中的最新 5 条记录：

`git reflog {{[-n|--max-count]}} 5`
