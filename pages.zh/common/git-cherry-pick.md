# git cherry-pick

> 将现有提交引入的更改应用到当前分支。
> 要将更改应用到其他分支，请先使用 `git checkout` 切换到所需的分支。
> 更多信息：<https://git-scm.com/docs/git-cherry-pick>。

- 将一个提交应用到当前分支：

`git cherry-pick {{commit}}`

- 将一系列提交应用到当前分支（另见 `git rebase --onto`）：

`git cherry-pick {{start_commit}}~..{{end_commit}}`

- 将多个（非连续的）提交应用到当前分支：

`git cherry-pick {{commit1 commit2 ...}}`

- 将提交的更改添加到工作目录，但不创建提交：

`git cherry-pick --no-commit {{commit}}`