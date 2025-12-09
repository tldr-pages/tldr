# git cherry-pick

> 将现有提交的变更应用到当前分支。
> 如需应用到其他分支，请先用 `git checkout` 切换到目标分支。
> 更多信息：<https://git-scm.com/docs/git-cherry-pick>.

- 将单个提交应用到当前分支：

`git cherry-pick {{提交哈希}}`

- 将连续多个提交应用到当前分支（也可参考 `git rebase --onto`）：

`git cherry-pick {{起始提交}}~..{{结束提交}}`

- 将多个（非连续的）提交应用到当前分支：

`git cherry-pick {{提交1 提交2 ...}}`

- 将提交变更应用到工作区但不自动创建提交：

`git cherry-pick {{[-n|--no-commit]}} {{提交哈希}}`
