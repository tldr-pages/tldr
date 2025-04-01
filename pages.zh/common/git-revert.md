# git revert

> 创建新的提交来撤销之前的提交效果。
> 更多信息：<https://git-scm.com/docs/git-revert>。

- 撤销最近的一次提交：

`git revert {{HEAD}}`

- 撤销第5次之前的提交：

`git revert HEAD~{{4}}`

- 撤销指定的提交：

`git revert {{0c01a9}}`

- 撤销多个提交：

`git revert {{branch_name~5..branch_name~2}}`

- 不创建新的提交，仅更改工作树：

`git revert {{[-n|--no-commit]}} {{0c01a9..9a1743}}`

- 在合并冲突后取消Git撤销：

`git revert --abort`