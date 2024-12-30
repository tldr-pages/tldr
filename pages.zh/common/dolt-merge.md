# dolt 合并

> 将两个或多个开发历史合并在一起。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-merge>。

- 将指定提交的更改合并到当前分支：

`dolt merge {{branch_name}}`

- 将指定提交的更改合并到当前分支，而不更新提交历史：

`dolt merge --squash {{branch_name}}`

- 合并一个分支并即使在快速前进的情况下也创建一个合并提交：

`dolt merge --no-ff {{branch_name}}`

- 合并一个分支并使用特定的提交信息创建合并提交：

`dolt merge --no-ff -m "{{message}}" {{branch_name}}`

- 中止当前的冲突解决过程：

`dolt merge --abort`