# dolt merge

> 合并两个或多个开发历史。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-merge>.

- 将指定提交的更改合并到当前分支：

`dolt merge {{branch_name}}`

- 将指定提交的更改合并到当前分支，但不更新提交历史：

`dolt merge --squash {{branch_name}}`

- 合并分支并创建合并提交，即使合并可以作为快进解决：

`dolt merge --no-ff {{branch_name}}`

- 合并分支并创建带有特定提交消息的合并提交：

`dolt merge --no-ff -m "{{message}}" {{branch_name}}`

- 中止当前的冲突解决过程：

`dolt merge --abort`