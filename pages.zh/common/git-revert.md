# git revert

> 创建新的提交，以逆转早期提交的效果。
> 更多信息：<https://git-scm.com/docs/git-revert>。

- 逆转最近的提交：

`git revert {{HEAD}}`

- 逆转倒数第5个提交：

`git revert HEAD~{{4}}`

- 逆转特定的提交：

`git revert {{0c01a9}}`

- 逆转多个提交：

`git revert {{branch_name~5..branch_name~2}}`

- 不创建新的提交，只改变工作树：

`git revert {{-n|--no-commit}} {{0c01a9..9a1743}}`