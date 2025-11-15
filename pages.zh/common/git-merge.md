# git merge

> 合并分支。
> 更多信息：<https://git-scm.com/docs/git-merge>.

- 将指定分支合并到当前分支：

`git merge {{分支名}}`

- 编辑合并说明信息:

`git merge {{[-e|--edit]}} {{分支名}}`

- 合并分支，创建合并提交：

`git merge --no-ff {{分支名}}`

- 遇到冲突时中止合并：

`git merge --abort`

- 采用特定的策略进行合并：

`git merge {{[-s|--strategy]}} {{策略}} {{[-X|--strategy-option]}} {{策略选项}} {{分支名}}`
