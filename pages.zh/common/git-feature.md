# git feature

> 创建或合并特性分支。
> 特性分支遵循格式 feature/name。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-feature>.

- 创建并切换到新的特性分支：

`git feature {{feature_branch}}`

- 将特性分支合并到当前分支，并创建合并提交：

`git feature finish {{feature_branch}}`

- 将特性分支合并到当前分支，并将更改压缩为一个提交：

`git feature finish --squash {{feature_branch}}`

- 将特定特性分支的更改推送到其远程对应分支：

`git feature {{feature_branch}} --remote {{remote_name}}`