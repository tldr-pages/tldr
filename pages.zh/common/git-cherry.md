# git cherry

> 查找尚未应用到上游分支的提交。
> 更多信息：<https://git-scm.com/docs/git-cherry>.

- 显示已在上游分支有对应提交的提交（包含提交信息）：

`git cherry {{[-v|--verbose]}}`

- 指定不同的上游分支和主题分支进行比较：

`git cherry {{上游分支}} {{主题分支}}`

- 限定比较范围到某个基准点之后的提交：

`git cherry {{上游分支}} {{主题分支}} {{基准点}}`
