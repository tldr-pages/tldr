# git 删除压缩合并的分支

> 删除已经“压缩合并”到指定分支的分支并切换到该分支。如果未指定分支，则默认为当前检出的分支。
> 属于 `git-extras`。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-delete-squashed-branches>。

- 删除所有已经“压缩合并”到当前检出分支的分支：

`git delete-squashed-branches`

- 删除所有已经“压缩合并”到指定分支的分支：

`git delete-squashed-branches {{branch_name}}`