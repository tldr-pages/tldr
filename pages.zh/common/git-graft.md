# git graft

> 将一个分支中的提交合并到另一个分支，并删除源分支。
> 这是 `git-extras` 的一部分。
> 更多信息：<https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- 将源分支中不在目标分支中的所有提交合并到目标分支，并删除源分支：

`git graft {{source_branch}} {{target_branch}}`